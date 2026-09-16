def close_client_stream(client_stream, unix_path):
    try:
        client_stream.shutdown(socket.SHUT_RDWR)
        if unix_path:
            logger.debug('%s: Connection closed', unix_path)
        else:
            peer = client_stream.getpeername()
            logger.debug('%s:%s: Connection closed', peer[0], peer[1])
    except (socket.error, OSError) as exception:
        logger.debug('Connection closing error: %s', exception)
    client_stream.close()