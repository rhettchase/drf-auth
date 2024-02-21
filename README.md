# LAB - Class 33

## Project: Authentication & Production Server

### Project Description

Fully functional CRUD API app that allows users to view the collection of brews (GET), as well as Create, Update, and Delete brews from the collection. Users are required to be authenticated to access the API. The app utilizes a Postgres database and is run in Docker container.

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [Django, Docker, and PostgreSQL Tutorial](https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial)
- [Django REST Framework - Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)

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
  - From admin panel you can also create new users (make them a Staff account to have access to admin panel)
- Add to brew collection by using a `POST` request

#### How to use your library (where applicable)

Once server is running, use Thunder Client or other application of your choice to complete GET, PUT, POST, DELETE Requests. GET requests also can be completed in the browser.

*Must be logged in to access the API*

- Login with superuser or staff user credentails at [`http://0.0.0.0:8000/admin/`](http://0.0.0.0:8000/admin/)
- Or authenticate in the `Auth` panel using Thunder Client or other comparable app

##### GET Requests (Read)

- [`http://0.0.0.0:8000/api/v1/brews`](http://0.0.0.0:8000/api/v1/brews/)

##### POST Requests (Add)

- User Thunder Client to add `body` > `JSON`, OR go to bottom of page [`http://0.0.0.0:8000/api/v1/brews/`](http://0.0.0.0:8000/api/v1/brews/)

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
- edit JSON body (see example above)
- Permissions required: only the user that created the specific brew may update it

##### DELETE Requests

- [`http://0.0.0.0:8000/api/v1/brews/{id}/`](http://0.0.0.0:8000/api/v1/brews/2/)
- Permissions required: only the user that created the specific brew may update it

#### Tests

- `docker compose run web python manage.py test`
