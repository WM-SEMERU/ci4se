def key(self):
    return [part.strip() for part in self.href.split('/') if part.strip()][-1]