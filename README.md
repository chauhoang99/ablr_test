Set up virtualenv

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

Run Django server

python manage.py runserver 3001  # Only port 3001 works, other ports will cause error on Singpass side.

Then access to localhost:3001 and try the tool.
