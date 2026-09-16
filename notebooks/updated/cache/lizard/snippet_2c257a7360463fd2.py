def _start_frontend(self, restart=False):
    self.log(self.config, self.config.frontendenabled, lvl=verbose)
    if self.config.frontendenabled and not self.frontendrunning or restart:
        self.log('Restarting webfrontend services on', self.frontendtarget)
        self.static = Static('/', docroot=self.frontendtarget).register(self)
        self.websocket = WebSocketsDispatcher('/websocket').register(self)
        self.frontendrunning = True