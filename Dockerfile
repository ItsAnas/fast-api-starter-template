FROM python:3.8-slim

EXPOSE 80

COPY ./src /docker-src/

WORKDIR /docker-src/

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
