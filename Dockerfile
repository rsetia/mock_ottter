FROM python:2

WORKDIR /usr/src/app

RUN pip install flask

COPY . .

ENV FLASK_APP ottter.py

ENV FLASK_RUN_HOST 0.0.0.0

CMD [ "flask", "run" ]

EXPOSE 5000
