def nack(self, delivery_tag=0, multiple=False, requeue=True):
    if not compatibility.is_integer(delivery_tag):
        raise AMQPInvalidArgument('delivery_tag should be an integer')
    elif not isinstance(multiple, bool):
        raise AMQPInvalidArgument('multiple should be a boolean')
    elif not isinstance(requeue, bool):
        raise AMQPInvalidArgument('requeue should be a boolean')
    nack_frame = specification.Basic.Nack(delivery_tag=delivery_tag,
        multiple=multiple, requeue=requeue)
    self._channel.write_frame(nack_frame)