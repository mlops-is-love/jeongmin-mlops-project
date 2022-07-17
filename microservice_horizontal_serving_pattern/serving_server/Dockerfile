FROM python:3.8

WORKDIR /workspace
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]