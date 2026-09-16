def hosts(self, **kwargs):
    kwargs['channelID'] = self.id
    return self.connection.listHosts(**kwargs)