def tag_info(self):
    return self.__class__.__name__ + ('(%r)' % self.name if self.name else ''
        ) + ': ' + self.valuestr()