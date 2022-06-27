FROM python:3.8

WORKDIR /app

# Install mlflow and packages requied to interact with PostgreSQL and MinIO
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt