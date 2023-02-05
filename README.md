# Fast Api sample

## Description

This is a sample project to learn how to use Fast Api framework and how to use it with mongodb.

## Pre-Requisites

* [Python 3.9](https://www.python.org/downloads/)
* Mongodb 4.4 or higher (for local development) or [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (for production) or docker image of mongodb (for local development)
* Docker (optional)

## Credit

* The code of this project is based on the tutorial of [MoureDev by Brais Moure](https://github.com/mouredev) : [Curso de PYTHON desde CERO para BACKEND](https://www.youtube.com/watch?v=_y9qQZXE24A&t=20500s)

## Documentation and references 

* [Python](https://www.python.org/doc/)
* [Fast Api](https://fastapi.tiangolo.com/) or [Fast Api Github](https://github.com/tiangolo/fastapi)
* [cryptography](https://python-jose.readthedocs.io/en/latest/)
* [swagger](https://swagger.io/) or [swagger-ui](https://swagger.io/tools/swagger-ui/)
* [http status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Installation

### Install from requirements.txt

```bash
    pip install -r requirements.txt
```

### Or Install dependencies of framework one by one

```bash
    pip install fastapi[all]
    pip install "python-jose[cryptography]"
    pip install "passlib[bcrypt]"
    pip install pymongo
```

## Run in local

in terminal run the following command
```bash 
    uvicorn main:app --reload
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redocs) with your browser to see the result.

## Build docker image

first build the docker image with the following command:
```bash
    docker build -t fastapi-sample .
```

## Run docker image

run the following command to run the docker image

```bash
    docker run -d -p 8000:8000 fastapi-sample
```
