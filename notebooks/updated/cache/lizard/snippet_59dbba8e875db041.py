def insecure_channel(target, options=None, *, loop=None, executor=None,
    standalone_pool_for_streaming=False):
    return Channel(_grpc.insecure_channel(target, options), loop, executor,
        standalone_pool_for_streaming)