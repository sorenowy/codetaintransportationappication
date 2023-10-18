# Codetain Transportation Route app
Codetain Recruitment Task

## Task description
An application that manages transport routes for registered users.

## Requirements
* Docker engine & docker compose / or Docker Desktop
* Python3 installed

## Components
* Webpanel - served by Angular - http://localhost:4200
* API - served by FastAPI - http://localhost:8000
* MailDev - opensource SMTP server - http://localhost:1080
* PostgreSQL db container - http://localhost:8774

## How to run via Docker
* Clone this repository
* Go to /deployment directory
* execute `docker-compose up -d --force-recreate --build`
* Enjoy!

## How to run locally
* Clone this repository
* Go to main directory of downloaded repository
* Create virtual environment for Python via `python -m venv venv`
* Activate 
* run command `prisma generate --schema ./app/database/prisma/schema.prisma` - to generate tables
* run command `uvicorn main:app --reload --port "port_of_choice"`
* build database and MailDev with docker
    *  `docker-compose build postgres-db`
    *  `docker-compose build maildev`
* Enjoy!

## How to run migrations (how to develop, maintain, fix this code :))
1. Add new entity, or changes in /database/prisma/schema.prisma
2. run command `prisma migrate dev --schema ./app/database/prisma/schema.prisma` - this will apply migrations and purge the database

## tests
* To run tests, simply go to /app folder, and execute `pytest` command.

## Swagger
Swagger is located at: http://localhost:8000/docs

## MailDev
It's an opensource SMTP server with graphical inbox hosted on http://localhost:1080 - it is used for validation purposes of registered users

## Troubleshooting tips
* If you cant connect to the webpanel, or Swagger, try checking your Docker containers. Simply shut down other containers, to ensure ports are free of use.