def transactions(self, **query):
    if 'status' in query and isinstance(query['status'], list):
        query['status'] = ','.join(map(str, query['status']))
    transaction_resource = self.resource.transactions(query)
    return Transactions(transaction_resource, self.client, populate=True)