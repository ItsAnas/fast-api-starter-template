FROM python:3.8-slim

EXPOSE 80

COPY ./src /docker-src/

RUN pip install -r docker-src/requirements.txt

WORKDIR /docker-src/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
