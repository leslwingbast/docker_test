FROM python:3.10-alpine

RUN pip install pandas

COPY . /app

WORKDIR /app

CMD ["python","./dockertest.py"]