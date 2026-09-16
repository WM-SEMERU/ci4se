def subscribe(self, transport, data):
    self.add(transport, address=data.get('hx_subscribe').encode())
    self.send(data['hx_subscribe'], {'message': '%r is listening' % transport})