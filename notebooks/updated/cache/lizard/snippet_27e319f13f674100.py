def declare(self, queue='', passive=False, durable=False, exclusive=False,
    auto_delete=False, arguments=None):
    if not compatibility.is_string(queue):
        raise AMQPInvalidArgument('queue should be a string')
    elif not isinstance(passive, bool):
        raise AMQPInvalidArgument('passive should be a boolean')
    elif not isinstance(durable, bool):
        raise AMQPInvalidArgument('durable should be a boolean')
    elif not isinstance(exclusive, bool):
        raise AMQPInvalidArgument('exclusive should be a boolean')
    elif not isinstance(auto_delete, bool):
        raise AMQPInvalidArgument('auto_delete should be a boolean')
    elif arguments is not None and not isinstance(arguments, dict):
        raise AMQPInvalidArgument('arguments should be a dict or None')
    declare_frame = pamqp_queue.Declare(queue=queue, passive=passive,
        durable=durable, exclusive=exclusive, auto_delete=auto_delete,
        arguments=arguments)
    return self._channel.rpc_request(declare_frame)