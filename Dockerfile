FROM python:3-alpine3.20
RUN apk add --no-cache bash shadow
RUN adduser -D -s /bin/bash appuser
RUN mkdir /app && chown appuser:appuser /app
WORKDIR /app
USER appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]
