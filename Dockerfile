FROM ros:foxy

# Install ROS 2 packages
RUN apt-get update && apt-get install -y \
    ros-foxy-rclpy \
    ros-foxy-std-msgs \
    ros-foxy-launch \
    ros-foxy-launch-ros \
    && rm -rf /var/lib/apt/lists/*
# Use an official Python runtime as a base image
FROM python:3.11.6

# Set the working directory in the container
WORKDIR /AI-RedBack/

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# The command to run when container is started
CMD ["python", "./src//app.py"]

