FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["pytest", "--cov=app", "--cov-report=xml", "--maxfail=1", "--disable-warnings", "&&", "gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
