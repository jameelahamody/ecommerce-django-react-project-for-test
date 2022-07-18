FROM python:3
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#WORKDIR /code
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#COPY . .
#CMD ["python", "manage.py","runserver"]


RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python-pip
RUN apt-get -y install python-pip
RUN pip install django==3.0

ENV PYTHONPATH $PYTHONPATH:/code
ENV app_port 8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE ${app_port}



COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]