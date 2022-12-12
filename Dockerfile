FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt 

COPY . .

EXPOSE 8000

RUN python3 manage.py migrate

CMD [ "python3","manage.py","runserver","0.0.0.0:8000" ]