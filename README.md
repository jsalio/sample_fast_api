# Fast Api sample

## Install

```bash
    pip install -r requirements.txt
```

### install dependencies of framework

```bash
    pip install fastapi[all]
    pip install sqlalchemy
    pip install psycopg2
    pip install python-dotenv
    pip install "python-jose[cryptography]"
    pip install "passlib[bcrypt]"
    pip install pymongo
```

## Create database

```bash
    python create_db.py
```

## Run

```bash 
    uvicorn main:app --reload
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redocs) with your browser to see the result.