def update(self, other_dict):
    for key, value in iter_multi_items(other_dict):
        MultiDict.add(self, key, value)