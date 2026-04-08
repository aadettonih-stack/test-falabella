FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PORT=8080

CMD ["functions-framework", "--target=hello_pubsub", "--signature-type=cloudevent", "--port=8080"]
