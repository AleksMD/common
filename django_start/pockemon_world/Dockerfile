FROM python:3.7
COPY . /app
RUN pip install django requests
WORKDIR /app
EXPOSE 8000
CMD python3 -m manage runserver
