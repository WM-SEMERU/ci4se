def _handle_sighup(myrpcserver, signum, unused):
    print('SIGHUP: stopping all clients', sys.stderr)
    if myrpcserver._closed:
        return
    for c in set(myrpcserver.clients):
        try:
            c.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        c.close()
    myrpcserver.clients.clear()