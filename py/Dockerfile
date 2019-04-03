# docker build -t arq-flask-app .
# docker run -p 8000:8000 arq-flask-app

FROM python:3.7.2

RUN mkdir /app
WORKDIR /app

COPY app.py .
COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv install --ignore-pipfile

ENTRYPOINT ["pipenv", "run", "gunicorn", "-w", "1", "app:app", "-b", "0.0.0.0:8000"]
