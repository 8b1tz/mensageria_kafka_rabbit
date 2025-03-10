import pika, json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='simple_email')

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Enviando email para: {data['email']} com mensagem: {data['email']}")

channel.basic_consume(queue='simple_email', on_message_callback=callback, auto_ack=True)

print('Esperando emails...')
channel.start_consuming()
