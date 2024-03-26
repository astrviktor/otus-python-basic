# docker build . -t app
# docker run -p 8000:8000 -it app
#FROM python:3.9-slim
FROM python:3.9.6-alpine3.14

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]