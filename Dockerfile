FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /usr/src/app/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend_config.wsgi:application"]


# Run the application using Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Run the application using Django's development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]