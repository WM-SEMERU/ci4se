def create_queue(self, Name, **kwargs):
    return int(self.edit_queue('new', Name=Name, **kwargs))