#!/usr/bin/env python
import os
import sys
import csv
from urllib.error import HTTPError
import urllib.request
from argparse import ArgumentParser

if __name__ == "__main__":
    """
    This bulk sample data tool takes in a pipe-separated values file containing
    questions, answers, and distractors and POSTs them to the questions REST API.
    """
    parser = ArgumentParser()
    parser.add_argument('file', help='Path to file containing sample data.')
    args = parser.parse_args()
    
    url = 'http://127.0.0.1:8000/questions/'
    
    csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)
    
    with open(args.file, "rt") as csvfile:
        for row in csv.DictReader(csvfile, dialect='piper'):
            # TODO: Needs better edge case handling
            # Pull question text and inferred type from the PSV
            text = row['question']
            if '+' in text:
                type = 'addition'
            elif '-' in text:
                type = 'subtraction'
            elif '*' in text:
                type = 'multiplication'
            elif '/' in text:
                type = 'division'
            else:
                print("Couldn't determine type of question; skipping...")
                continue
            
            # Pull answer and distractors info from the PSV, and create an array of JSON answers
            answer_template = r'{{"value" : {0}, "is_correct" : "{1}"}}'
            answer = answer_template.format(row['answer'], 'True')
            answers = [answer,]
            for distractor in row['distractors'].split(','):
                answers.append(answer_template.format(distractor.strip(), 'False'))
            
            # Create final JSON question, including all potential answers
            question_template = r'{{"text" : "{0}", "type" : "{1}", "answers" : [{2}]}}'
            question = question_template.format(text, type, ", ".join(answers))
            
            # Send data to server via POST to REST API
            binary_data = question.encode('ascii')
            req = urllib.request.Request(url, binary_data, {'Content-Type': 'application/json'})
            try:
                response = urllib.request.urlopen(req)
                result = response.read()
                # print(result)
                response.close()
            except HTTPError as e:
                print('Error while loading sample data. Got code: ' + str(e.code) + ' and message: ' + str(e.read()))