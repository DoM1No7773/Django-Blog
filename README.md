# Django-Blog

## How to download?

Download the repository:

```bash
git clone https://github.com/DoM1No7773/Django-Blog.git
```

## How to run?


Download and install [docker-engine](https://docs.docker.com/engine/install/) 


Build a docker image:

```bash
docker build -t <image name> .
```

Run the application:

```bash
docker run -it -p 8000:8000 -d <image name>
```

Create superuser account:
```bash
docker exec -it <container-id> python manage.py createsuperuser
```

Open a browser, type localhost:8000 and check if it's working.
