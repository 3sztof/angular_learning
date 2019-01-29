import pika
import uuid

class FibonacciRpcClient(object):
    # Konstruktor klasy
    def __init__(self):
        # Nawiazanie polaczenia
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        # Wygenerowanie unikatowej kolejki: callback_queue z losowym id
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        # Subskrybcja callback_queue, nasluchiwanie odpowiedzi RPC
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    # Jesli otrzymam odpowiedz z odpowiednim correlation id, przerywa nasluichiwanie i zapisuje response do self.response
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    # RPC request: wysyla request do glownej kolejki rpc_queue wraz z informacja gdzie odpowiedziec i z jakim kluczem corr_id
    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        # Czeka na odpowiedz, kiedy sie pojawi, zwraca ja pod funkcja fubonacci_rpc.call(n)
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)