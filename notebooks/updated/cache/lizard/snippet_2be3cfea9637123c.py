def get_raise_list(self, data):
    return_list = []
    lst = self.get_list_key(data, 'raise')
    for l in lst:
        name, desc, _ = l
        return_list.append((name, desc))
    return return_list