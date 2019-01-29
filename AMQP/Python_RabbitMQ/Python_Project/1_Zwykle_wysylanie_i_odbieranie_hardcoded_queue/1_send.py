import pika


# Skrót do obiektu - kanału - nawiązanie połączenia
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# Moje: input: nazwa kolejki
kolejka = input("Podaj nazwe kolejki: ")

# Deklaracja kolejki - nie usuwa istniejącej, więc warto robić za każdym razem
channel.queue_declare(queue=kolejka)


# Moje: input: tekst wiadomości
wiadomosc = input("Wpisz wiadomosc: ")

# Funkcja publikująca wiadomość "Hello World!" do kolejki "hello", domyślny exchange (wysle to tylko do kolejki hello - key)
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=wiadomosc)
print(" [x] Wyslano:", wiadomosc)


# Zakończenia połączenia
connection.close()