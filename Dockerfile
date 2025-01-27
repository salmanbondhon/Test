# Use the official Python base image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies explicitly
RUN pip install protobuf==3.20.0 altair[vegalite]

# Copy the rest of your application code into the container
COPY . /app/

# Expose the port your application will run on
EXPOSE 8501

# Command to run your application
CMD ["streamlit", "run", "app.py"]
