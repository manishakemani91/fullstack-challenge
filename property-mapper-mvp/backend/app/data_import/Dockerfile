FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

ENV PYTHONPATH=/app
COPY ./app/data_import/requirements.txt /app/requirements.txt
COPY ./app/data_import/data.xlsx /app/data.xlsx
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./app /app
CMD ["python", "/app/data_import/import_data.py"]

