FROM python:3.9-slim
LABEL authors="zhichliu"git

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "flask_q.py"]