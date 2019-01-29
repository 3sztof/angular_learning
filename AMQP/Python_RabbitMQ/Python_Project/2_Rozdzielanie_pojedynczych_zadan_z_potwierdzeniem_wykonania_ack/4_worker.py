import pika
import time


# Nawiazanie polaczenia
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# Redundantna deklaracja kolejki trwalej task_queue (nie zniknie przy reboocie); uwaga: nie mozna zmienic typu wczesniej zadeklarowanej kolejki
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


# Gdy otrzyma wiadomosc, pisze Received oraz czeka tyle sekund, ile kropek zawierala wiadomosc, nastepnie wysyla wiadomosc ack() o przetworzeniu zadania
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


# QoS - konsumuje tylko jedna wiadomosc na raz, poki nie wysle ack, nie przyjmie nic wiecej od brokera kolejki
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')


# Am am
channel.start_consuming()