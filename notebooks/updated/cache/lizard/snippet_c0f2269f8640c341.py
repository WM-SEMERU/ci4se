def create_server(addr, port, backlog):
    server = Spin()
    server.bind((addr, port))
    server.listen(backlog)
    Server(server)
    server.add_map(ACCEPT, lambda server, spin: install_basic_handles(spin))
    return server