def get_mentions(self, *args, **kwargs):
    return self.get_content(self.config['mentions'], *args, **kwargs)