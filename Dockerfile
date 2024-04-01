FROM python:3.9

WORKDIR calisma_alani

COPY . .

RUN pip install flask gunicorn

ENTRYPOINT ["gunicorn", "index:app"]
