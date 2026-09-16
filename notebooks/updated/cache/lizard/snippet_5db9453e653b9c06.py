def init(port=6600, server='localhost'):
    client = mpd.MPDClient()
    try:
        client.connect(server, port)
        return client
    except ConnectionRefusedError:
        print('error: Connection refused to mpd/mopidy.')
        os._exit(1)