FROM python:3.10-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]