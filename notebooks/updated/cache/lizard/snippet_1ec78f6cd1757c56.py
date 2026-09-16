def publish(cls, message, client_filter=None):
    with cls._lock:
        for client in cls.subscribers:
            if not client_filter or client_filter(client):
                client.send(message)