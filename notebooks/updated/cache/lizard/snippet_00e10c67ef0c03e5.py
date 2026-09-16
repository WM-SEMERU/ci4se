def checkState(self):
    if self.data is True:
        return Qt.Checked
    elif self.data is False:
        return Qt.Unchecked
    else:
        raise ValueError('Unexpected data: {!r}'.format(self.data))