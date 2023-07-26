# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Expose the port that Flask is running on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
