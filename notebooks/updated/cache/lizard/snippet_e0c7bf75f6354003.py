def load_key(self, path):
    with open(path, 'r') as f:
        self.key = f.readline().strip()
        self.secret = f.readline().strip()