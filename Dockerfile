# Use the NVIDIA CUDA 12.3.2 base image with Ubuntu 20.04
FROM nvidia/cuda:12.3.2-base-ubuntu20.04

# Install Python, pip, and other necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Flask and PyTorch
RUN pip3 install Flask torch torchvision

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app to the container
COPY app.py /app

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
