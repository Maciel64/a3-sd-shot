FROM python:3.12-slim

# Evita .pyc e melhora logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório da aplicação
WORKDIR /app

# Instala dependências primeiro (melhora cache)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Start da aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]