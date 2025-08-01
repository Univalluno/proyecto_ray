FROM python:3.10-slim

RUN apt-get update && apt-get install -y gcc curl

WORKDIR /app

COPY main.py .
COPY core/ core/

RUN pip install --upgrade pip && pip install "ray[serve]" fastapi uvicorn

CMD ["python3", "main.py"]
