def get_inbox(self, *args, **kwargs):
    return self.get_content(self.config['inbox'], *args, **kwargs)