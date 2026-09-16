def load_data(self, filename, *args, **kwargs):
    if not filename.endswith('.json'):
        filename += '.json'
    with open(filename, 'r') as fid:
        json_data = json.load(fid)
    if not self.orig_data_reader or isinstance(self, self.orig_data_reader):
        return self.apply_units_to_cache(json_data['data'])
    utc_mod_time = json_data.get('utc_mod_time')
    orig_data_reader_obj = self.orig_data_reader(self.parameters, self.meta)
    if utc_mod_time:
        utc_mod_time = time.struct_time(utc_mod_time)
        orig_filename = filename[:-5]
        if utc_mod_time < time.gmtime(os.path.getmtime(orig_filename)):
            os.remove(filename)
            return orig_data_reader_obj.load_data(orig_filename)
    return orig_data_reader_obj.apply_units_to_cache(json_data['data'])