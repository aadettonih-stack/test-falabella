FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

WORKDIR /app

# 1. Copiamos requisitos e instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copiamos TODO el proyecto (incluyendo la carpeta src/)
COPY . .

# 3. Configuramos el PYTHONPATH para que Python encuentre la carpeta 'src'
ENV PYTHONPATH=/app

# 4. CMD ajustado:
# --source es la ruta relativa al archivo desde el WORKDIR
CMD ["functions-framework", "--target=main", "--source=src/main.py", "--signature-type=cloudevent", "--host=0.0.0.0", "--port=8080"]