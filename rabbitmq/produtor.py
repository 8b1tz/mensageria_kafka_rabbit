import pika, json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='simple_email')

message = {"email": "user@domain.com", "subject": "Bem-vindo", "body": "Olá usuário!"}
channel.basic_publish(
    exchange='',
    routing_key='simple_email',
    body=json.dumps(message)
)
print("Mensagem enviada à fila!")
connection.close()