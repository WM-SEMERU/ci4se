def get_all(self):
    logger.debug('Fetching items. Path: {data_file}'.format(data_file=self.
        data_file))
    return load_file(self.client, self.bucket_name, self.data_file)