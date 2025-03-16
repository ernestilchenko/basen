# Use Python 3.11 as base image (compatible with Django 5.1)
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=basen.settings

# Install system dependencies including gettext for internationalization
RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /app

# Copy requirements file first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Compile translation messages
RUN python manage.py compilemessages

# Collect static files
#RUN python manage.py collectstatic --noinput

# Make migrations and migrate database
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose port for the Django development server
EXPOSE 8000

# Command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]