import pika
import sys


# Nawiazanie polaczenia
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# Deklaracja exchange'a typu fanout (przesle wszystko co otrzyma do kazdej znanej mu kolejki - routing key "")
channel.exchange_declare(exchange='logs',
                         type='fanout')


# Okreslenie wiadomosci - wpisany argument lub Hello World
message = ' '.join(sys.argv[1:]) or "info: Hello World!"


# Okreslenie publikowania do exchange'a logs
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)


connection.close()