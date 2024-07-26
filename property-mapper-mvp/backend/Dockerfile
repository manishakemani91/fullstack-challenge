FROM python:3.10-slim-bullseye


RUN apt-get update \
  && apt-get -y install libpq-dev gcc curl procps net-tools tini \
  && apt-get -y clean \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./requirements.txt
RUN pip install gunicorn --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r ./requirements.txt

WORKDIR /app
COPY . .
COPY alembic.ini /app/alembic.ini

RUN ls -l

EXPOSE 8000