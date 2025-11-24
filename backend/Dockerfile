# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy backend source code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Expose port 8000
EXPOSE 8000

# Start FastAPI with uvicorn
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
