# Use official Python image
FROM python:3.12.10

# Expose port 5000 inside container
EXPOSE 5000

# Set working directory
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy project files
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Command to run Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
