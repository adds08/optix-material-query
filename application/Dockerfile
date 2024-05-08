FROM python:3.8-slim-buster

# Install git
RUN apt-get update && apt-get install -y git

WORKDIR /app

# Clone the repository into the /app directory
RUN git clone https://github.com/adds08/optix-material-query .

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Set the working directory to the application folder
WORKDIR /app/application

# Command to run the Flask application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
