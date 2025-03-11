# Use the official Python 3.8 slim image as the base image
 FROM python:3.11-slim

 # Set the working directory within the container
 WORKDIR /libresail

 # Copy the necessary files and directories into the container
 COPY resources/ templates/ .venv main.py requirements.txt /libresail/
 COPY .venv application.py requirements.txt  /libresail/

 # Upgrade pip and install Python dependencies
 RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

 # Expose port 5000 for the Flask application
 EXPOSE 5000

 # Define the command to run the Flask application using Gunicorn
 CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000", "-w", "4"]
