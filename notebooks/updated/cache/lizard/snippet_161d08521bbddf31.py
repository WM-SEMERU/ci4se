def new_item(self, hash_key, range_key=None, attrs=None):
    return Item(self, hash_key, range_key, attrs)