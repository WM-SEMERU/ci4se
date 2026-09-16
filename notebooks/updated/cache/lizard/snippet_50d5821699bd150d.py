def add(self, item):
    check_not_none(item, "item can't be none")
    return self._encode_invoke(transactional_set_add_codec, item=self.
        _to_data(item))