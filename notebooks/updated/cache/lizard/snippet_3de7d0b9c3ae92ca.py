def SearchClients(query=None, context=None):
    args = client_pb2.ApiSearchClientsArgs(query=query)
    items = context.SendIteratorRequest('SearchClients', args)
    return utils.MapItemsIterator(lambda data: Client(data=data, context=
        context), items)