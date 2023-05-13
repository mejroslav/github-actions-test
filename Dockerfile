FROM python:3.10-alpine

WORKDIR /app

COPY * /app/

CMD ["python3", "main.py"]