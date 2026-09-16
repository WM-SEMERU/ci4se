def register(cls, encryptor: Encryptor):
    cls.__encryptor__ = encryptor
    listeners = dict(init=on_init, load=on_load)
    for name, func in listeners.items():
        if contains(cls, name, func):
            remove(cls, name, func)
        listen(cls, name, func)