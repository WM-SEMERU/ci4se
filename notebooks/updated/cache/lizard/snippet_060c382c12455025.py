def get(self, event):
    self.log('Schemarequest for', event.data, 'from', event.user, lvl=debug)
    if event.data in schemastore:
        response = {'component': 'hfos.events.schemamanager', 'action':
            'get', 'data': l10n_schemastore[event.client.language][event.data]}
        self.fireEvent(send(event.client.uuid, response))
    else:
        self.log('Unavailable schema requested!', lvl=warn)