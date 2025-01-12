FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password
ENV MYSQL_DB=weather_db

CMD ["python", "app.py"]
