# Imagine de bază
FROM python:3.10-slim

# Setează directorul de lucru
WORKDIR /app

# Copiază fișierele proiectului în container
COPY requirements.txt .

# Instalează dependențele
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Rulează botul
CMD ["python", "bot.py"]
