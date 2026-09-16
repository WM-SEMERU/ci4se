def index_record(self, json_path):
    self.logger.debug('Indexing record: %s', json_path)
    json_path = os.path.abspath(json_path)
    self.check_path(json_path, '`json_path`')
    with open(json_path) as fp:
        try:
            dct = json.load(fp)
        except ValueError:
            warnings.warn('Ignoring invalid JSON file at: {0}'.format(
                json_path))
            return
    record_type = self.get_record_type(json_path)
    kwds = {}
    if record_type == 'command':
        importer = self.db.import_dict
        kwds.update(check_duplicate=self.check_duplicate)
    elif record_type == 'init':
        importer = self.db.import_init_dict
    elif record_type == 'exit':
        importer = self.db.import_exit_dict
    else:
        raise ValueError('Unknown record type: {0}'.format(record_type))
    importer(dct, **kwds)
    if not self.keep_json:
        self.logger.info('Removing JSON record: %s', json_path)
        os.remove(json_path)