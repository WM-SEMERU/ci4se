def change_id(self, new_id):
    self._load_raw_content()
    self._id = new_id
    self.get_filename(renew=True)
    self.get_filepath(renew=True)
    return