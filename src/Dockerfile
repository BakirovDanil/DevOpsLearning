FROM python:3.13
WORKDIR /usr/local/app

ENV HTTP_PROXY="http://proxy50.0002.pfr.ru:8080"
ENV HTTPS_PROXY="http://proxy50.0002.pfr.ru:8080"

COPY . /usr/local/app

RUN pip install --no-cache-dir -r /usr/local/app/requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]