FROM python:3

RUN pip install pandas

COPY . /app

WORKDIR /app

CMD ["python","./dockertest.py"]