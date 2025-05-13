FROM python:3.9-slim

# Set workdir
WORKDIR /app

# Copy semua file
COPY . .

# Pindah ke folder app saat run
WORKDIR /app/app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r ../requirements.txt

# Jalankan app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
