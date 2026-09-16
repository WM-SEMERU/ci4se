def pop(self, name):
    if name in self:
        new_name = self.var_case_name(name)
        if new_name in self.keys():
            output = self[new_name]
            self.data.drop(new_name, inplace=True, axis=0)
        else:
            output = self.ho_data.pop(new_name)
        return output
    else:
        raise KeyError('Key not present in metadata variables')