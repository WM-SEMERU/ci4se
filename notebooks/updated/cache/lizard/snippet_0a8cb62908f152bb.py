def configuration(self, event):
    try:
        self.log('Schemarequest for all configuration schemata from', event
            .user.account.name, lvl=debug)
        response = {'component': 'hfos.events.schemamanager', 'action':
            'configuration', 'data': configschemastore}
        self.fireEvent(send(event.client.uuid, response))
    except Exception as e:
        self.log('ERROR:', e)