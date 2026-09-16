def create_exchange(self):
    channel = self._connect_mq()
    channel.exchange_declare(exchange=self.user.prv_exchange, exchange_type
        ='fanout', durable=True)