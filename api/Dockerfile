# Imagen base oficial de Python
FROM python:3.10-slim

# Evitar prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y gcc curl

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos del servicio y lógica paralela
COPY main.py .
COPY core/ core/

# Instalar dependencias de Python
RUN pip install --upgrade pip && pip install "ray[serve]" fastapi uvicorn

# Exponer el puerto de la API
EXPOSE 8000

# Comando para iniciar el servicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
