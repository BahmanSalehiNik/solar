FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .


ENTRYPOINT ["python3", "app.py"]


