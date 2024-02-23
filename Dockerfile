# First stage: Build interactsh-client
FROM golang:1.17 AS builder

RUN go install github.com/projectdiscovery/interactsh/cmd/interactsh-client

# Second stage: Python base image to run Flask application
FROM python:3.8-slim

WORKDIR /app

COPY --from=builder /go/bin/interactsh-client /usr/local/bin/interactsh-client

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
