def init(port=8813, numRetries=10, host='localhost', label='default'):
    _connections[label] = connect(port, numRetries, host)
    switch(label)
    return getVersion()