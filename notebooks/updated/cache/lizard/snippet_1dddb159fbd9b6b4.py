def getlist(self, event):
    try:
        componentlist = model_factory(Schema).find({})
        data = []
        for comp in componentlist:
            try:
                data.append({'name': comp.name, 'uuid': comp.uuid, 'class':
                    comp.componentclass, 'active': comp.active})
            except AttributeError:
                self.log('Bad component without component class encountered:',
                    lvl=warn)
                self.log(comp.serializablefields(), pretty=True, lvl=warn)
        data = sorted(data, key=lambda x: x['name'])
        response = {'component': 'hfos.ui.configurator', 'action':
            'getlist', 'data': data}
        self.fireEvent(send(event.client.uuid, response))
        return
    except Exception as e:
        self.log('List error: ', e, type(e), lvl=error, exc=True)