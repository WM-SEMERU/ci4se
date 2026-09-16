def get_client(client_id):
    client = Client.query.get(client_id)
    if client and client.user.active:
        return client