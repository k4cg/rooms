# Rooms

## Setup:
* Install local jitsi instance (e.g., using docker-compose)
* Install python requirements: `pip install -r requirements.txt `
* go to directory `/rooms/rooms`
* copy `config.py.template` to `config.py` and fill in config details
* go to `/rooms`
* create database: `python manage.py migrate`
* create initial backend user: `python manage.py createsuperuser`
* start `./runserver`
* visit http://localhost:8080 (hint `http://127.0.0.1:8080` doesn't work)
