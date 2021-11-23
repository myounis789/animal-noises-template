# Dockerfile for a Python App
FROM python:3.6

COPY . .

RUN pip install -r requirements.text

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]