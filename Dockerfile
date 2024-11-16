FROM python:3.10.8-slim

RUN apt-get update && \
    apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY ./models /app/models

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 8000

ENV HOST=0.0.0.0 PORT=8000

CMD ["uvicorn", "fastApiPY:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]