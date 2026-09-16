def connect(signal, receiver):
    __check_receiver(receiver)
    if __is_bound_method(receiver):
        ref = WeakMethod
    else:
        ref = weakref.ref
    with __lock:
        __purge()
        __receivers[signal].append(ref(receiver))