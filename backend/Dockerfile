# pull official base image
FROM python:3.10
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /backend
COPY Pipfile* /backend/

# Copy the cron job file into the image
COPY cron_import_api_data /etc/crontabs/root
# Set execution permissions
RUN chmod 0644 /etc/crontabs/root

RUN pip install gunicorn
RUN pip install pipenv
RUN pipenv sync --system           

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=brucetrader.settings

# copy project
COPY . /backend/

RUN chmod +x /backend/docker-entrypoint.sh

# Run the cron-like scheduler and your Python script
CMD ["sh", "-c", "crond && tail -f /backend/logs/cron.log"]
ENTRYPOINT [ "/backend/docker-entrypoint.sh" ]
