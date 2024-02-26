# pull official base image
FROM python:3.10
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /backend
COPY Pipfile* /backend/

RUN pip install gunicorn
RUN pip install pipenv
RUN pipenv sync --system           

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=brucetrader.settings

# copy project
COPY . /backend/

RUN chown -R 1000:1000 /backend/logs
RUN chmod +x /backend/docker-entrypoint.sh

ENTRYPOINT [ "/backend/docker-entrypoint.sh" ]
