def _validate(self, writing=False):
    if self.brand not in ['jp2 ', 'jpx ']:
        msg = (
            "The file type brand was '{brand}'.  It should be either 'jp2 ' or 'jpx '."
            )
        msg = msg.format(brand=self.brand)
        if writing:
            raise IOError(msg)
        else:
            warnings.warn(msg, UserWarning)
    for item in self.compatibility_list:
        if item not in self._valid_cls:
            msg = (
                'The file type compatibility list {items} is not valid.  All items should be members of {valid_entries}.'
                )
            msg = msg.format(items=self.compatibility_list, valid_entries=
                self._valid_cls)
            if writing:
                raise IOError(msg)
            else:
                warnings.warn(msg, UserWarning)