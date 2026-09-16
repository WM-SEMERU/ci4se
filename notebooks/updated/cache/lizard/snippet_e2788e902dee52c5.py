def wait_return(self, callback):
    if self.check_recv():
        return callback(self)
    _t = threading.Thread(target=self._wait_non_ressources, args=(callback,))
    _t.setDaemon(True)
    _t.start()