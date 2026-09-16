def sendcommand(self, name, **kwargs):
    self.log('sending command %s(**%s)' % (name, kwargs))
    self.channel.send((name, kwargs))