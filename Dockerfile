FROM python:3-alpine3.20
RUN useradd -m -s /bin/bash appuser
RUN mkdir /app && chown appuser:appuser /app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
USER appuser
EXPOSE 5000
CMD ["python", "main.py"]
