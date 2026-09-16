def save(self, filename=None, clean_data=False, raw=False, trash=False):
    full_path = get_filename(filename or self.filename or self.name, trash)
    data = raw and self.raw_data or self.data
    if clean_data:
        data = self.clean_data(data)
    with open(full_path, 'w') as fn:
        if filename.endswith('.json'):
            fn.write(json.dumps(data, indent=2, separators=(',', ': ')))
        else:
            fn.write(str(data))
    self.filename = full_path
    return full_path