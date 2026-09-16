def handle_error(_, client_addr):
    exc_type, exc_value, _ = sys.exc_info()
    if exc_type is socket.error and exc_value[0] == 32:
        pass
    elif exc_type is cPickle.UnpicklingError:
        sys.stderr.write('Invalid connection from {0}\n'.format(client_addr[0])
            )
    else:
        raise