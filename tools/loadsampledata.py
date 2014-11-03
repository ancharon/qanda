#!/usr/bin/env python
import os
import sys
import csv
from urllib.error import HTTPError
import urllib.request
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('file', help='Path to file containing sample data.')
    args = parser.parse_args()
    
    url = 'http://127.0.0.1:8000/questions/'
    
    csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)
    
    with open(args.file, "rt") as csvfile:
        for row in csv.DictReader(csvfile, dialect='piper'):
            # Needs better edge case handling
            question = r'{{"text" : "{0}", "type" : "{1}", "answers" : [{2}]}}'
            text = row['question']
            if '+' in text:
                type = 'ADD'
            elif '-' in text:
                type = 'SUB'
            elif '*' in text:
                type = 'MUL'
            elif '/' in text:
                type = 'DIV'
            else:
                print("Couldn't determine type of question; skipping...")
                continue
            answer_template = r'{{"value" : {0}, "is_correct" : "{1}"}}'
            answer = answer_template.format(row['answer'], 'True')
            answers = [answer,]
            for distractor in row['distractors'].split(','):
                answers.append(answer_template.format(distractor.strip(), 'False'))
            question = question.format(text, type, ", ".join(answers))
            
            binary_data = question.encode('ascii')
            req = urllib.request.Request(url, binary_data, {'Content-Type': 'application/json'})
            try:
                response = urllib.request.urlopen(req)
                result = response.read()
                # print(result)
                response.close()
            except HTTPError as e:
                print('Error while loading sample data. Got code: ' + str(e.code) + ' and message: ' + str(e.read()))