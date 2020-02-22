FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir -p /usr/local/application
COPY ./app/ /usr/local/application/
COPY ./requirements.txt /usr/local/application/requirements.txt
RUN pip install -r /usr/local/application/requirements.txt && \
    rm -f /usr/local/application/requirements.txt
EXPOSE 5000

WORKDIR /usr/local
CMD ["gunicorn", "application.manage:app", "-c", "application/config/gunicorn_setting.py"]
