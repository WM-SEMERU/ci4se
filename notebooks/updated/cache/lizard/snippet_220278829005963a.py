def create_db(self):
    if self.db_type != 'json':
        raise RuntimeError('db_type only supports json now')
    if os.path.exists(self.json_db_path):
        return False
    if os.path.exists(self.factory_json_db_path):
        with self.db_mutex:
            shutil.copy2(self.factory_json_db_path, self.json_db_path)
        return True
    _logger.debug('*** NO such file: %s' % self.factory_json_db_path)
    raise RuntimeError('No *.json.factory file')