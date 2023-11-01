FROM python:3.10
ENV PYTHONBUFFERED 1
WORKDIR /app

COPY requirements.txt /app	

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "8000"]