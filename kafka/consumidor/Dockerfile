# Usa imagem oficial Python 3.12 slim
FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Instala dependências
RUN pip install --upgrade pip
RUN pip install kafka-python

# Copia script consumidor
COPY consumer_monitor.py .

# Comando padrão (consumidor Kafka com monitoramento)
CMD ["python", "consumer_monitor.py"]
