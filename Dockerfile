# Gunakan image Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Salin requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin source code
COPY . .

# Jalankan aplikasi FastAPI dengan Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
