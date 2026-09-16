def get_servers_list(self):
    ret = []
    if self.args.browser:
        ret = self.static_server.get_servers_list()
        if self.autodiscover_server is not None:
            ret = self.static_server.get_servers_list(
                ) + self.autodiscover_server.get_servers_list()
    return ret