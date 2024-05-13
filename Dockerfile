# Use the Python 3.11.4 base image
FROM python:3.11.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 5000  # Change to your desired port number

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory in the container to /app
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which your Flask app will run
EXPOSE $PORT

# Command to run the Flask application using Gunicorn
CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:$PORT", "app:app"]
