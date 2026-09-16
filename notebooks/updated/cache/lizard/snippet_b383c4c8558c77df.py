def connect(server, password=None, factory_class=VNCDoToolFactory, proxy=
    ThreadedVNCClientProxy, timeout=None):
    if not reactor.running:
        global _THREAD
        _THREAD = threading.Thread(target=reactor.run, name='Twisted',
            kwargs={'installSignalHandlers': False})
        _THREAD.daemon = True
        _THREAD.start()
        observer = PythonLoggingObserver()
        observer.start()
    factory = factory_class()
    if password is not None:
        factory.password = password
    family, host, port = command.parse_server(server)
    client = proxy(factory, timeout)
    client.connect(host, port=port, family=family)
    return client