# Async First Step for FastAPI
This repo is nothing more than instructions for the first level of a FastAPI app. Fork the repo.

# Goal
The goal of this repo is to prepare for, and experiment with, a FastAPI fully asynchronous app. Some of the basics have been filled in to both keep things consistent and to alleviate the initial gear-up. Once the basics are established, new development is simple.

## Endpoints
To at least somewhat represent asynchronous database lookups and inserts we will need a couple endpoints configured. 

### GET:  `/notifications/v1/{notification_id}`
This should return the given Notification object or a 404 if it is not found.

### POST: `/notifications/v1/`
This endpoint should take in a payload such as:
```json
    {
        "to": "example@gmail.com",
        "personalization": {
            "band": "Incubus"
        }
    }
```
The return should be the Notification object created.

### POST: `/notifications/v1/multiple`
This endpoint should take in a payload such as:
```json
    [
        {
            "to": "example@gmail.com",
            "personalization": {
                "band": "Korn"
            }
        },
        {
            "to": "another-example@gmail.com",
            "personalization": {
                "band": "Soundgarden"
            }
        }
    ]
```
The return should be the Notification objects created.

# Installation Instructions
Since [fastapi0](https://github.com/k-macmillan/fastapi0) dealt with the Poetry setup this one comes fully-functional. You only need to run:
```bash
    poetry install --with static_tools
```
This will allow your editor to use `.venv/bin/python` for the interpretter for proper intellisense. You can also enter the `poetry shell` to perform style checking.


# Style Checking
Style checking is defined in `pyrpoject.toml` and can be executed with the following commands:
```
    flake8 --select=DCO020 fastapi1
    mypy fastapi1 --strict
    ruff check fastapi1
```

Alternatively, you can check all at once with `./scripts/run_checks.sh`. It is advised that an effort is made to get the checks to pass when the code is complete (maybe starting with the incomplete functions that mypy identifies).

# Starting Point
Most of the application is already setup. The [fastapi1/status](fastapi1/status) folder contains some example code. The [fastapi1/notifications/v1/](fastapi1/notifications/v1/) folder has an outline to start from.

## Fill Outline
The application will start as-is but it is missing any real functionality other than a heartbeat endpoint. Feel free to start it before filling in the outline. To have it fully functioning to store notifications in the DB you'll need to add the missing pieces that would come with building an app of this type. You do not have to follow the outline that is given, but it is recommended.

## Container Start
To bring the container up:
```bash
    docker compose -f ci/docker-compose-local.yml up
```
It will start with a single uvicorn worker. You can then follow the URL FastAPI gives you to open the docs. it should be something such as http://localhost:8000/docs#. 

Executing the heartbeat GET request should show the following in your docker container:
```log
    app-1  | INFO:     172.18.0.1:57406 - "GET /status/heartbeat HTTP/1.1" 204 No Content
    app-1  | INFO:     GET http://localhost:8000/status/heartbeat 204 0.014161s
```

# Testing
Once the `/notifications/v1/` route is established with the required endpoints testing can begin! Much like `fastapi0`, this will use locust to performance test.

Start the container and in another terminal start locust:
```bash
    locust --processes 4
```
Point the [locust](http://localhost:8089) host to your app URL. Navigate to the GUI and try `60` users, `10` ramp up, and `30s` for the advanced settings (run time).

The [locustfile.py](locustfile.py) has several methods commented out. Try a couple different configurations. Record your results and identify how you can get the most notifications per time interval into the database.

# Challenge
Templates and Services were a bit beyond the scope, but would be good to also loop in. If you are up for the challenge bring them into `models.py`, `dao_methods.py`, and appropriate routes. Aim for [4NF](https://en.wikipedia.org/wiki/Fourth_normal_form); the `Notifications` table is not 4NF currently!
