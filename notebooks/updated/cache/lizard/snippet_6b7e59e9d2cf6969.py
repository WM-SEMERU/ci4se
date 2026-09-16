def api_client(connection, client_class=xbahn.api.Client):
    return client_class(link=xbahn.connection.link.Link(receive=connection,
        send=connection))