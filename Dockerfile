FROM python:3.9-slim

# Arbeitsverzeichnis
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Anwendung kopieren
COPY . .

# Flask starten
CMD ["python", "app.py"]
