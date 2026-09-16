def get_type(self):
    for typechar, typename in self.KEY_TYPE_CHOICES:
        if typechar == self.key_type:
            return typename