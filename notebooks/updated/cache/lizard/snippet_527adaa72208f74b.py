def assign(self, key, value):
    key_split = key.split('.')
    cur_dict = self
    for k in key_split[:-1]:
        try:
            cur_dict = cur_dict[k]
        except KeyError:
            cur_dict[k] = self.__class__()
            cur_dict = cur_dict[k]
    cur_dict[key_split[-1]] = value