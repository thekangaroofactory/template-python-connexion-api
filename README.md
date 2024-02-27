# Python / Connexion - Flask / API

- Using connexion framework (to build the Flask API)
- API key authentication
- SQLAlchemy + PostgresSQL database
- Wrapped in Docker container
- Served with gunicorn (using ASGI server / see connexion doc)


## Running:

### From python

`$ python app.py`

Now open your browser and go to http://localhost:8080/openapi/ui/ or 
http://localhost:8080/swagger/ui/ to see the Swagger UI.

The local hardcoded apikey is asdf1234567890.

Test it out (in another terminal):

`curl -X 'GET' 'http://localhost:8080/openapi/resources' -H 'accept: application/json' -H 'X-Auth: asdf1234567890'`

### In Docker

Build the Docker image:

`docker build -t template .`

Run the image in a container:\
Note that Dockerfile has `CDM` binding port to `"-b 0.0.0.0:10000"` (because of Render expecting that)

`docker run --name templateapp -p 10000:10000 template`

Now open your browser and go to http://localhost:10000/openapi/ui/ or 
http://localhost:10000/swagger/ui/ to see the Swagger UI.

The local hardcoded apikey is asdf1234567890.

Test it out (in Powershell >= 7):

`curl -X 'GET' 'http://localhost:10000/openapi/resources' -H 'accept: application/json' -H 'X-Auth: asdf1234567890'`
