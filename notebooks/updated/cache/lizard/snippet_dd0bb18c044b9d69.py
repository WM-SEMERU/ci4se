def shape(self):
    if len(self) == 0:
        return ()
    elif self.is_power_space:
        try:
            sub_shape = self[0].shape
        except AttributeError:
            sub_shape = ()
    else:
        sub_shape = ()
    return (len(self),) + sub_shape