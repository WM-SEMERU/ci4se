def get_config_items(self):
    return ('settings', self.settings), ('context_class', self.context_class
        ), ('interfaces', self.interfaces), ('logging', self.logging), ('name',
        self.name), ('init_handler', self.init_handler), ('sigusr1_handler',
        self.sigusr1_handler), ('sigusr2_handler', self.sigusr2_handler)