# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /opt

# Copy the current directory contents into the container at /app
COPY . /opt

COPY requirements.txt /opt/requirements.txt

# Install required Python modules
RUN pip install -r /opt/requirements.txt

# Define environment variable
ENV NAME CheckIP

# Run python script when the container launches
CMD ["python3", "main.py"]
