# Base image
FROM python:3.6.13

# Work directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy your application code 
COPY . . 

# Command to start the FastAPI server 
CMD ["python", "main_with_proxy.py"]