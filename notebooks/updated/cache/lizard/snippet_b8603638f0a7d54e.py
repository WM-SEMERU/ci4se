def stop_daemon(self, payload=None):
    kill_signal = signals['9']
    self.process_handler.kill_all(kill_signal, True)
    self.running = False
    return {'message': 'Pueue daemon shutting down', 'status': 'success'}