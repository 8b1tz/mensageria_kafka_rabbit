# 🚀 Exemplos de Messageria

Este repositório contém dois exemplos claros e detalhados sobre como trabalhar com sistemas de mensageria usando Python:

1. **Exemplo Simples (RabbitMQ)**
2. **Exemplo Complexo (Kafka)** com geração de relatórios em tempo real.

## 🐰 Exemplo Simples com RabbitMQ

Neste exemplo, utilizamos o RabbitMQ para demonstrar uma comunicação simples baseada em filas.

### Estrutura do Projeto:

```
rabbitmq/
├── Dockerfile
├── produtor.py
└── consumidor.py
```

### Como executar

1. Instale e execute o RabbitMQ localmente ou usando Docker:

```bash
docker run -d --hostname rabbit-local --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

2. Build do container Python:

```bash
docker build -t rabbitmq-produtor ./rabbitmq
```

3. Execute o produtor e consumidor:

```bash
docker run --network host rabbitmq-produtor
```

### Dependências:
- `pika`

## 🐳 Exemplo Complexo com Kafka e Monitoramento em Tempo Real

Este exemplo ilustra um sistema robusto e escalável utilizando Apache Kafka, com múltiplos tópicos e monitoramento dinâmico de mensagens recebidas, processadas e pendentes.

### Estrutura do Projeto:

```
kafka/
├── produtor/
│   ├── Dockerfile
│   └── producer.py
└── consumidor/
    ├── Dockerfile
    └── consumer_monitor.py
```

### Setup Kafka rápido com Docker Compose

Crie um arquivo `docker-compose.yml` na raiz:

```yaml
version: '3'
services:
  zookeeper:
    image: wurstmeister/zookeeper
    ports:
      - "2181:2181"

  kafka:
    image: wurstmeister/kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: localhost
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
```

Execute:

```bash
docker-compose up -d
```

### Como executar produtor e consumidor

Build:

```bash
docker build -t kafka-produtor ./kafka/produtor
docker build -t kafka-consumidor ./kafka/consumidor
```

Run:

```bash
# Executar produtor
docker run --network host kafka-produtor

# Executar consumidor com monitoramento em tempo real
docker run --network host kafka-consumidor
```

### Dependências:
- `kafka-python`

---

## 📌 Comparação dos Exemplos

| Característica       | RabbitMQ (Simples) | Kafka (Complexo)            |
|----------------------|--------------------|-----------------------------|
| Escalabilidade       | Baixa/Média        | Alta                        |
| Formatos de mensagem | JSON               | JSON, Avro, ProtoBuf        |
| Robustez             | Básica             | Alta (Retries, Logs, Acks)  |
| Monitoramento        | Manual             | Automático, em tempo real   |

---

## 🔧 Tecnologias Usadas

- Python 3.12
- RabbitMQ (Pika)
- Apache Kafka (Kafka-Python)
- Docker & Docker Compose

---

## 📚 Documentação adicional

- [Documentação Oficial RabbitMQ](https://www.rabbitmq.com/)
- [Documentação Oficial Kafka](https://kafka.apache.org/)
