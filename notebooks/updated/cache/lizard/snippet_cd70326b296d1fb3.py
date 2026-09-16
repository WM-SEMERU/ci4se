def delete(self, exchange='', if_unused=False):
    if not compatibility.is_string(exchange):
        raise AMQPInvalidArgument('exchange should be a string')
    delete_frame = pamqp_exchange.Delete(exchange=exchange, if_unused=if_unused
        )
    return self._channel.rpc_request(delete_frame)