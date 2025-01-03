FROM python:3.12-slim

WORKDIR /test

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=test.py
ENV FLASK_END=production


CMD ["flask", "run", "--host=0.0.0.0"]