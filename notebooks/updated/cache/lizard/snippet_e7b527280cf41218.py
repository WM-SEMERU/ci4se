def set_unlock_previous(self, unlock_previous):
    if unlock_previous is None:
        raise NullArgument('unlock_previous cannot be None')
    if unlock_previous is not None and not utilities.is_string(unlock_previous
        ):
        raise InvalidArgument('unlock_previous must be a string')
    self.my_osid_object_form._my_map['unlockPrevious'] = unlock_previous