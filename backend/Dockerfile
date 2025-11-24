FROM python:3.10-slim

WORKDIR /app

# Kopjojmë vetëm requirements fillimisht
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Tani kopjojmë gjithë backend-in
COPY . .

# Ekspozojmë portin
EXPOSE 8000

CMD ["python", "main.py"]
