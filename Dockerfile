FROM python:3.9

WORKDIR calisma_alani

COPY . .

RUN apt update -y

RUN apt install npm -y

RUN pip install flask gunicorn

ENTRYPOINT ["gunicorn", "index:app"]
