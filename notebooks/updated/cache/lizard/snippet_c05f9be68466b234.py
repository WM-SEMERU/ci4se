def reset(self):
    for _, item in self.iter_items(recursive=True):
        item.reset()