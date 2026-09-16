def setProperty(self, full_path, protect, dummy=7046):
    data = {'orgresource': full_path, 'protect': protect, 'userid': self.
        user_id, 'useridx': self.useridx, 'dummy': dummy}
    s, metadata = self.POST('setProperty', data)
    if s is True:
        return True
    else:
        return False