def send(socket, data, num_bytes=20):
    pickled_data = pickle.dumps(data, -1)
    length = str(len(pickled_data)).zfill(num_bytes)
    socket.sendall(length.encode())
    socket.sendall(pickled_data)