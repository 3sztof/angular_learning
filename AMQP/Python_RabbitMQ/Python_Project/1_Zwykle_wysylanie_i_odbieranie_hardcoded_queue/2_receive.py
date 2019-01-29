import pika


# Skrót do obiektu - kanału - nawiązanie połączenia
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# Deklaracja kolejki - nie usuwa istniejącej, warto robić w każdym połączeniu
channel.queue_declare(queue='hello')


# Definicja funkcji wypisującej informacje o odebraniu wiadomości
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# Ustawienie opcji konsumowania z danej kolejki
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()