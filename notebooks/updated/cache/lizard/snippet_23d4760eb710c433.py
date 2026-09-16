def _get_file_paths(self, tax_ids, file_type):
    file_paths = dict()
    if file_type not in self.files:
        raise KeyError('file type {} not configured'.format(file_type))
    for taxon in tax_ids:
        file_paths[taxon] = {'file': '{}.{}'.format(taxon, self.files[
            file_type]['pattern']), 'url': '{}{}.{}'.format(self.files[
            file_type]['path'], taxon, self.files[file_type]['pattern']),
            'headers': {'User-Agent': USER_AGENT}}
    return file_paths