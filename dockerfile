# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy requirements.txt if you have dependencies
COPY requirements.txt .


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files into the container
COPY . .

# Run main.py when container starts
CMD ["python", "main.py"]
