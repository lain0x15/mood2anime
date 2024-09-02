FROM python:3.12-slim

COPY ./mood2anime /mood2anime

WORKDIR /mood2anime

RUN pip install -r ./requirements.txt && python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]