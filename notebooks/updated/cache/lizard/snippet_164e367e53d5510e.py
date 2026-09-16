def run_process(self, analysis, action_name, message='__nomessagetoken__'):
    if action_name == 'connect':
        analysis.on_connect(self.executable, self.zmq_publish)
    while not analysis.zmq_handshake:
        yield tornado.gen.sleep(0.1)
    log.debug('sending action {}'.format(action_name))
    analysis.zmq_send({'signal': action_name, 'load': message})
    if action_name == 'disconnected':
        yield tornado.gen.sleep(0.1)
        analysis.on_disconnected()