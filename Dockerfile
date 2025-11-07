FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# RUN pip install --no-cache-dir --timeout-200 --retries=5 -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.org/simple --timeout=200 --retries=5

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
