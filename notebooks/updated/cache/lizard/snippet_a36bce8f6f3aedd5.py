def get_all_fields(self, arr):
    for k, v in self.fields.items():
        arr.append(v)
    if self.extends:
        parent = self.contract.get(self.extends)
        if parent:
            return parent.get_all_fields(arr)
    return arr