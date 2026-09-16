def mark_all_as_read(self, recipient=None):
    qset = self.unread(True)
    if recipient:
        qset = qset.filter(recipient=recipient)
    return qset.update(unread=False)