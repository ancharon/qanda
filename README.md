qanda - smarterer code challenge
=====
Ethan Caldwell


Setup
=====
It is suggested but not required that virtualenv be used to isolate the dependencies this project requires.
If you choose not to use it, skip the first two steps.

Steps to run:
  virtualenv env
  source env/bin/activate

  pip install django
  pip install djangorestframework
  pip install django-filter

  cd <path to qanda>

  python manage.py syncdb
  python manage.py runserver

At this point the qanda server should be up and ready for requests as a development server.

Sample Data
===========
To load the sample data supplied with the code challenge, run the loadsampledata.py tool included in this package.

  cd tools
  python loadsampledata.py smarterer_code_challenge_question_dump.psv

This may take a minute or two, as it calls the API for each question instead of writing directly to DB.

API Use
=======
Once the server is up, the API is fully browsable at http://127.0.0.1:8000/
However, as an overview here are some basic operations allowed:

http://127.0.0.1:8000/questions/
  GET # returns a list of all questions, defaulting to 20/page
      # can filter questions by 'text' or 'type' by adding ?text=<foo> or ?type=<bar>
      # can search question text by adding ?search=<baz>
      # can order questions by 'text' or 'type' by adding ?ordering=text or ?ordering=type
      # (use '-text'/'-type' to reverse order)
  POST # creates a new question, including child answers

http://127.0.0.1:8000/questions/#/
  GET # returns a single question, by ID
  PUT # updates existing question
  DELETE # removes existing question, cascade deletes child answers

http://127.0.0.1:8000/answers/
  GET # returns a list of all answers, defaulting to 20/page
      # can filter answers by 'value' adding ?value=<foo>
      # can order answers by 'value' by adding ?ordering=value
      # (use '-value' to reverse order)
  POST # creates a new answer (must be tied to existing parent question)

http://127.0.0.1:8000/answers/#/
  GET # returns a single answer, by ID
  PUT # updates existing answer
  DELETE # removes existing answer

All of these support the OPTIONS verb for additional usage documentation.
