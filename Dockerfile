# Use the Python image
FROM python:3.9-slim

# Install system dependencies required for lightgbm
RUN apt-get update && apt-get install -y libgomp1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copy the source code
COPY . .

# Run FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
