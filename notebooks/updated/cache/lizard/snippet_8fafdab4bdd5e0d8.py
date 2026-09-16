def wire(self, name, receive=None, send=None, respond=None, **kwargs):
    if hasattr(self, name) and name != 'main':
        raise AttributeError(
            "cannot use '%s' as name for wire, attribute already exists")
    if send:
        self.log_debug("Wiring '%s'.send: %s" % (name, send))
    if respond:
        self.log_debug("Wiring '%s'.respond: %s" % (name, respond))
    if receive:
        self.log_debug("Wiring '%s'.receive: %s" % (name, receive))
    wire = Wire(receive=receive, send=send, respond=respond)
    wire.name = '%s.%s' % (self.name, name)
    wire.meta = kwargs.get('meta', {})
    wire.on('receive', self.on_receive)
    setattr(self, name, wire)
    if not self.main:
        self.main = wire
    return wire