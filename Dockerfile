FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y ca-certificates

COPY docker/zscaler-root.cer \
     /usr/local/share/ca-certificates/zscaler-root.crt

RUN update-ca-certificates

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]