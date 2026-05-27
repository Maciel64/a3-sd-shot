FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# =========================
# SYSTEM DEPENDENCIES
# =========================
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    cmake \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1 \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# =========================
# PYTHON DEPENDENCIES
# =========================
COPY requirements.txt .

# evita crash de memória durante build pesado
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy==1.26.4 && \
    pip install --no-cache-dir -r requirements.txt

# =========================
# APP
# =========================
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]