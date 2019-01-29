import pika
import sys


# Nawiazanie polaczenia
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# Deklaracja direct exchange - skieruje logi tylko do kolejki o danym routing_key (binding)
channel.exchange_declare(exchange='direct_logs',
                         type='direct')


# Wczytuje pierwszy parametr skryptu jako waznosc - mo?liwe s? info (domyslny), warning, error (error ma specjalny queue)
severity = sys.argv[1] if len(sys.argv) > 2 else 'info'

# Wiadomosc to pozostale parametry skryptu
message = ' '.join(sys.argv[2:]) or 'Hello World!'


# Publish z zadanym routing_key
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()