FROM python:3.8.0-alpine3.10
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src src
COPY labels.json .

ENTRYPOINT ["python", "src/main.py"]
