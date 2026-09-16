def is_pending(self):
    self.get_info()
    if 'status' not in self.info:
        return False
    if 'isPending' not in self.info['status']:
        return False
    return self.info['status']['isPending']