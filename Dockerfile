FROM python:3.10-slim

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt --upgrade

COPY app /app

# You should use an ASGI server instead of a WSGI server. (see connexion doc)
CMD ["gunicorn", "-k uvicorn.workers.UvicornWorker", "-b 0.0.0.0:10000", "app:app"]
