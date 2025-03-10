from kafka import KafkaProducer
import json, random, time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

topics = ['pedidos', 'pagamentos', 'emails']

for i in range(1, 101):
    topic = random.choice(topics)
    message = {
        "id": i,
        "type": topic,
        "content": f"Mensagem {i}",
        "timestamp": time.time()
    }
    producer.send(topic=topic, value=message)
    print(f"Mensagem {i+1} enviada para {topic}")
    time.sleep(0.5)  # simula produção espaçada
