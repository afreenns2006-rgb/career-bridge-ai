# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose application port
EXPOSE 8501

# Run application
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]