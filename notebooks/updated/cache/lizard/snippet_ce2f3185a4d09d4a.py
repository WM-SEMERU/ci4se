def load_weights(self):
    if self.network_weights_loader:
        self.network_weights = self.network_weights_loader()
        self.network_weights_loader = None