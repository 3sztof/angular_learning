import pika
import sys


# Nawiazanie polaczenia
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# Deklaracja exchange direct - routing wiadomosci do danej kolejki
channel.exchange_declare(exchange='direct_logs',
                         type='direct')


# Deklaracja kolejki dla danego odbiorcy - generowana automatycznie nazwa, routing_key nadany dalej
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue


# Pobranie kolejnych parametrow - kluczy subskrybcji danych logow - routing_key
severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)


# Bind stworzonej kolejki do wczytanych routing_key
for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


# Definicja funkcji przy konsumpcji, print nazwy zdarzenia i opisu
def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()