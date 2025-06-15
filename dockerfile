# Gunakan image dasar dari Python
FROM python:3.8-slim

# Set working directory di dalam container
WORKDIR /app

# Copy file dari lokal ke dalam container
COPY . /app

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Perintah default untuk menjalankan aplikasi
CMD ["python", "eda_of_netflix_dataset.py"]
