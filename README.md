# Student Tutor Meets

In this project we have two main services:

- `web`
- `database`

We utilise Docker to easily run these services on different developers machines, and to keep our dependencies all in sync.

The web service is where our app's code runs, and the database stores persistent data which our app fetches.

We also have the `adminer` service which can be used to view the database in a more visual manner at http://localhost:8080.


## How to run the app

You will need to install [Docker](https://www.docker.com/products/docker-desktop/) on your machine.

Once you have it installed, open the root directory of the application (where `compose.yml` is) and type:

    docker compose up

You should now be able to visit the web app running at http://localhost:8000.

To exit you can hit `Ctrl+C` in your terminal, or open a new terminal at the same directory location and run:

    docker compose down


## How to run command inside the services

With Django, we often want to use the command line script `manage.py` to interact with our app. To open a shell alongside the web server, run:

    docker exec -it student_tutor_meets-web-1 bash

Then we can call various Django commands using `manage.py`

Connect to the Django shell:

    python manage.py shell

Migrate the database:

    python manage.py migrate

Create a new super user:

    python manage.py createsuperuser

These commands are all explained in [part 2](https://docs.djangoproject.com/en/5.0/intro/tutorial02/) of the [Writing your first Django app](https://docs.djangoproject.com/en/5.0/intro/tutorial01/) tutorial.

You can also run commands directly by replacing the `bash` part of the command above with any command you'd like to run alongside the service.

For example if we want to run the tests, we can run:

    docker exec -it student_tutor_meets-web-1 python manage.py test
