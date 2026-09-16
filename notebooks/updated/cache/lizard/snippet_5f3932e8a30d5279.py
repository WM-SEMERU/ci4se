def delete(self, queue='', if_unused=False, if_empty=False):
    if not compatibility.is_string(queue):
        raise AMQPInvalidArgument('queue should be a string')
    elif not isinstance(if_unused, bool):
        raise AMQPInvalidArgument('if_unused should be a boolean')
    elif not isinstance(if_empty, bool):
        raise AMQPInvalidArgument('if_empty should be a boolean')
    delete_frame = pamqp_queue.Delete(queue=queue, if_unused=if_unused,
        if_empty=if_empty)
    return self._channel.rpc_request(delete_frame)