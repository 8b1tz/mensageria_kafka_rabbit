from kafka import KafkaConsumer
import json
import threading
from collections import defaultdict

class KafkaConsumerService:
    def __init__(self, topics):
        self.consumer = KafkaConsumer(
            *topics,
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest',
            group_id='consumidor_grupo',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        self.total_messages = {topic: 0 for topic in topics}
        self.processed_messages = {topic: 0 for topic in topics}

    def process_messages(self):
        for msg in self.consumer:
            topic = msg.topic
            self.total_messages[topic] += 1
            print(f"Processando {msg.value} do tópico {topic}")
            time.sleep(random.uniform(0.3, 1.5))  # simula processamento variável
            self.processed_messages[topic] += 1

    def monitor(self):
        while True:
            time.sleep(5)
            print("\n--- Relatório em Tempo Real ---")
            for topic in self.total_messages:
                recebidas = self.total_messages[topic]
                processadas = self.processed_messages[topic]
                pendentes = recebidas - processadas
                print(f"Tópico '{topic}': Recebidas: {recebidas} | Processadas: {processadas} | Na fila: {pendentes}")
            print("------------------------------\n")

consumer = KafkaConsumerService(['pedidos', 'pagamentos', 'emails'])

# Inicia consumidor em thread separada
import threading

thread_process = threading.Thread(target=consumer.process_messages)
thread_monitor = threading.Thread(target=consumer.monitor)

thread_process.start()
thread_monitor.start()
