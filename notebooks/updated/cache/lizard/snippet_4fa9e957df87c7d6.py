def receive(socket, num_bytes=20):
    length = int(_receive_all(socket, num_bytes).decode())
    serialized_data = _receive_all(socket, length)
    return pickle.loads(serialized_data)