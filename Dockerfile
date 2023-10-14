# Use the official TensorFlow Docker image as the base image
FROM tensorflow/tensorflow:latest-gpu-jupyter

# Set the working directory in the container
WORKDIR /app

# Copy your application code and files into the container
COPY . /app

# (Optional) Install any additional dependencies using pip, for example:
# RUN pip install some-package

# Specify the command to run your TensorFlow application
# CMD ["python", "your_script.py"]
