def get_due(self, estimated):
    due = 0
    due = round((estimated - datetime.utcnow()).seconds / 60)
    return due