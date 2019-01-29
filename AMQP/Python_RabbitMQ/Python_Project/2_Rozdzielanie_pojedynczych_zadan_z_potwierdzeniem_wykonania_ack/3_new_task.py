import pika
import sys


# Nawiazanie polaczenia
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# Deklaracja trwalej kolejki task_queue - nie zostanie usunieta nawet przy reboocie
channel.queue_declare(queue='task_queue', durable=True)


# Wiadomosc wpisywana jako parametr skryptu: ilosc kropek w wiadomosci to ilosc sekund, jaka bedzie czekal - "pracowal" skrypt worker.py
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent (wiadomosc nie zostanie skasowana poki nie zostanie potwierdzone jej przetworzenie przez worker.py - ack()
                      ))
print(" [x] Sent %r" % message)
connection.close()