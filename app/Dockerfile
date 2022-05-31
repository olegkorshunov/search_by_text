FROM python:3.10
RUN mkdir -p /app
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
#CMD ["python","main.py"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
