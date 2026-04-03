# Imagen base oficial de Python
FROM python:3.11-slim

# Configuraciones para evitar basura de Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    REFLEX_ENV=prod

# Crear y movernos al directorio de la app
WORKDIR /app

# Instalar dependencias primero (Para aprovechar caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del portafolio
COPY . .

# Exponer el puerto por default de Hugging Face Spaces
EXPOSE 7860

# Correr ÚNICAMENTE el Backend asegurando que use el puerto 7860
CMD ["reflex", "run", "--env", "prod", "--backend-only", "--backend-port", "7860"]
