def _form_loader(self, _):
    data = {}
    for key in self.request.arguments:
        val = self.get_arguments(key)
        if len(val) == 1:
            data[key] = val[0]
        else:
            data[key] = val
    return data