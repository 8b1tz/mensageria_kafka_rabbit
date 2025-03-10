# Usa imagem oficial do Python 3.12 slim
FROM python:3.12-slim

# Diretório de trabalho
WORKDIR /app

# Instala dependências
RUN pip install --upgrade pip
RUN pip install pika

# Copia scripts Python para dentro do container
COPY produtor.py .
COPY consumidor.py .

# Comando padrão ao executar o container
CMD ["python", "produtor.py"]
