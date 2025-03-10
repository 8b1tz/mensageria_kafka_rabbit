# Usa imagem oficial Python 3.12 slim
FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Instala dependências
RUN pip install --upgrade pip
RUN pip install kafka-python

# Copia script produtor
COPY producer.py .

# Comando padrão (produtor Kafka)
CMD ["python", "producer.py"]
