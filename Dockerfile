FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
#DEPENDENCIES
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /code/