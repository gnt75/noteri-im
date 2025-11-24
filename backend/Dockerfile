FROM python:3.10

# Vendosim direktorinë e punës
WORKDIR /app

# Kopjojmë vetëm backend-in në container
COPY backend/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ekspozojmë portin (8000 nëse ke uvicorn)
EXPOSE 8000

# Komanda startuese — path i saktë
CMD ["python", "app/main.py"]
