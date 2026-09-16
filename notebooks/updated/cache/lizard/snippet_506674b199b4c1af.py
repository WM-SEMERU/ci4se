def call_closers(self, client, clients_list):
    for func in self.closers:
        func(client, clients_list)