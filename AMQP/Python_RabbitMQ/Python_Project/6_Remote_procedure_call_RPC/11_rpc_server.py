import pika


# Nawiazanie polaczenia i deklaracja kolejki rpc_queue
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


# Definicja funkcji rekursywnej licz?cej dany wyraz ci?gu Fibonacci'ego
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Przy zapytaniu wczytuje body jako argument funkcji fib(), po czym wysy?a odpowied? do kolejki identyfikowanej przez props.reply_to; to jest callback - wykonywany, kiedy przyjdzie request
def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)


# Przyjmuje 1 request na raz, z kolejki rpc_queue
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()