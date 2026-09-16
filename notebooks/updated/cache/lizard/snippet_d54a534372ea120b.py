def stop_tracking_host(self):
    try:
        self.server.hosts.remove(self.client_address[0])
        if hasattr(self.server.module, 'on_shutdown'):
            self.server.module.on_shutdown(self.server.context, self.server
                .connection)
    except ValueError:
        pass