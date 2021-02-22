# fast-api-starter-template

Starter project for an api with FastAPI.
This repository provides the minimum needed to create an API in Python.

⚠ Be carefull, this project is not (yet) production use.

## Requirements

- Python3
- pip3
- uvicorn
- Docker
- Docker Compose
- venv

## How to use it

### Fix the project name

Some fixme are present to have a generic app. They should be in 
`docker-compose.yml` and `src/app/data/db.py`. It will allows you to rename 
the project with a custom name.

> To find them easily: `grep -r fixme`

### For development

```bash
docker-compose up db # Create a postgresql instance with docker
cd app
./run.sh # Create a vitural env and run the app with guvicorn
```

Then, go to localhost:8000

### With Docker

```bash
docker-compose up
```

## TODO

- [x] Create a FastAPI app
- [x] Architecture correctly the app
- [x] Dockerize the app
- [x] Add a user model
- [ ] Hash passwords
- [ ] Login and JWT token
- [ ] Alembic migrations

## Known Issues

- If you run the project for the first time with docker, the database will take some to be created. Since the app needs it, it might crash the first time. When running `docker-compose up` a second time it will be fine.


## Other

Pull Request are welcomed