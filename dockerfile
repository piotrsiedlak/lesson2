FROM python:3-alpine3.20
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && apt-get update && apt-get install -y libssl1.0.0
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]
