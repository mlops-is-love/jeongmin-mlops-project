FROM python:3.8

WORKDIR /workspace
COPY . .

RUN apt-get update && apt-get install libgl1-mesa-glx -y
RUN pip install -r requirements.txt

ENV AWS_ACCESS_KEY_ID AKIARNA5NJ5334RA7IEK
ENV AWS_SECRET_ACCESS_KEY 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
ENV AWS_DEFAULT_REGION ap-northeast-2
ENV MLFLOW_TRACKING_URI http://15.164.49.19:5000

ENTRYPOINT [ "python3", "main.py" ]