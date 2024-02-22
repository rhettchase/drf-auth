# LAB - Class 33

## Project: Authentication & Production Server

### Project Description

Fully functional CRUD API app that allows users to view the collection of brews (GET), as well as Create, Update, and Delete brews from the collection. Users are required to be authenticated (via Basic authentication or JWT) to access the API. The app utilizes a Postgres database and is run in Docker container. The app includes JWT authentication to the API and a Gunicorn server. Whitenoise is used to handle static files.

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [Django, Docker, and PostgreSQL Tutorial](https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial)
- [Django REST Framework - Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
- [Gunicorn](https://gunicorn.org/)
- [Whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html)

### Setup

#### To run in Docker

- Install Docker Desktop and verify installation
  - Run `docker --version` and `docker-compose --version` to ensure both are correctly installed.

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- `PORT` - 8000

#### How to initialize/run your application (where applicable)

- Clone repo
- Install dependencies (see above)
- See the page in browser by running `docker-compose up --build`
- Open the page in the localhost specified in the terminal to view GET request and add `/api/v1/brews` to end of url
- Create superuser: `docker compose exec web python manage.py createsuperuser`
  - From admin panel [`http://0.0.0.0:8000/admin/`](http://0.0.0.0:8000/admin/) you can also create new users (make them a Staff account to have access to admin panel)
- Add to brew collection by using a `POST` request

#### How to use your library (where applicable)

Once server is running, use Thunder Client or other application of your choice to complete GET, PUT, POST, DELETE Requests. GET requests also can be completed in the browser. *Must be authenticated to access the API*

#### Tests (Thunder Client)

1. Get Access and Refresh Tokens

- complete `POST` request `0.0.0.0:8000/api/token/` to get access and refresh tokens
- input the username and password of the superuser you created in the `JSON` tab

```json
{
	"username": "admin",
	"password": "admin"
}
```

Response will include a "refresh" and an "access" token

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODY0MjU2MywiaWF0IjoxNzA4NTU2MTYzLCJqdGkiOiIzZGMyZDU0MWYyMGU0NTNmYmRhZmI4YWI1MzI1YjgwZSIsInVzZXJfaWQiOjF9.NNw_KuyaM5IHJtfJuKChZnj5p0HJz0OP58aVBGAHqpY",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4NTU2NDYzLCJpYXQiOjE3MDg1NTYxNjMsImp0aSI6IjdhODA0ZDdhZThmZjRmNzA5MDk1NzY5Y2U1ZGQ0MTYxIiwidXNlcl9pZCI6MX0.Vw6vo8rKDJFlGIa7hWYaxz06L06j1GtL0_EFNzo0r4s"
}
```

2. GET request with token authorization

- Copy the "access" token
- Create new `GET` request `http://0.0.0.0:8000/api/v1/brews/`
- Copy the "access" token into the `Auth` tab > `Bearer` tab in body called `Bearer Token`
- Send Request
- Response will be the list of all brews that have been added to the database

When this short-lived `access token` expires, you can use the longer-lived refresh token to obtain another access token:

3. Refresh access token

- Copy the "refresh" token
- Create new `POST` request
- In the JSON tab, copy the refresh code using the below format
- Send Request

```json
{
  "refresh": 
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODY0Mjk5NSwiaWF0IjoxNzA4NTU2NTk1LCJqdGkiOiJmZWI0MTNjMjFiODY0OTRjOTZlN2Q0ZDY4NmRmNTVjYiIsInVzZXJfaWQiOjF9.0PtwU1iJNmQbtMPdpDNNHiaNGPPEWJXaOZR1KcmtWbE"
}
```

Response will be a new access token, which you can use for new `GET` request

```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4NTYxODYyLCJpYXQiOjE3MDg1NTY1OTUsImp0aSI6IjU5NTI5ZThmZDc1NDRjMjJhOWM1NWFiZDBhZWYxZjFjIiwidXNlcl9pZCI6MX0.kikXTgUyInqIJQCgFz1BIYBleSVOCebvkhLLs2Ahl3M"
}
```

#### CRUD Routes

Note: Basic authentication is available for the CRUD routes (username and password)

##### GET Requests (Read)

- [`http://0.0.0.0:8000/api/v1/brews`](http://0.0.0.0:8000/api/v1/brews/)

##### POST Requests (Add)

- User Thunder Client to add `body` > `JSON` using below json format, OR go to bottom of page [`http://0.0.0.0:8000/api/v1/brews/`](http://0.0.0.0:8000/api/v1/brews/)
- In `Auth` tab > `Basic`, include username and password

```json
{
    "owner": 1,
    "name": "Vanilla Porter",
    "brew_type": "ST",
    "brewery": "Breckenridge Brewery",
    "description": "Aromas of vanilla and toasted grain set the stage for mellow flavors of vanilla and dark roasted malts in this popular porter."
}
```

##### PUT Requests (Update)

- [`http://0.0.0.0:8000/api/v1/brews/{id}/`](http://0.0.0.0:8000/api/v1/brews/2/)
- edit `JSON` body (see example above)
- Permissions required: only the user that created the specific brew may update it
- In `Auth` tab > `Basic`, include username and password

##### DELETE Requests

- [`http://0.0.0.0:8000/api/v1/brews/{id}/`](http://0.0.0.0:8000/api/v1/brews/2/)
- Permissions required: only the user that created the specific brew may update it
- In `Auth` tab > `Basic`, include username and password
