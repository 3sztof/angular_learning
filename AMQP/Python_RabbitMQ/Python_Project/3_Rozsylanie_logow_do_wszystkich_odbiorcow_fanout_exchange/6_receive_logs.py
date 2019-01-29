import pika


# Nawiazanie polaczenia
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# Redundantna definicja exchange typu fanout
channel.exchange_declare(exchange='logs',
                         type='fanout')


#  Okreslenie wygenerowanej automatycznie (exclusive) unikatowej kolejki pod queue_name - tylko ten ziomek bedzie otrzymywal z niej dane, a exchange bedzie wysylal do kazdej wygenerowanej przez konsumentow kolejki
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue


# Przywiazanie kolejki do exchange'a
channel.queue_bind(exchange='logs',
                   queue=queue_name)


# Debug
print(' [*] Waiting for logs. To exit press CTRL+C')


# Callback
def callback(ch, method, properties, body):
    print(" [x] %r" % body)


# Definicja konsumowania bez potwierdzen z dedykowanej kolejki
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()