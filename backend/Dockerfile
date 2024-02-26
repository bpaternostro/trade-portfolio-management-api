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

RUN chmod +x /backend/docker-entrypoint.sh

# Run the Python script
CMD ["python", "manage_import_all.py"]

ENTRYPOINT [ "/backend/docker-entrypoint.sh" ]
