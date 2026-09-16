def files(self, entity_id, manifest=None, filename=None, read_file=False,
    channel=None):
    if manifest is None:
        manifest_url = '{}/{}/meta/manifest'.format(self.url, _get_path(
            entity_id))
        manifest_url = _add_channel(manifest_url, channel)
        manifest = self._get(manifest_url)
        manifest = manifest.json()
    files = {}
    for f in manifest:
        manifest_name = f['Name']
        file_url = self.file_url(_get_path(entity_id), manifest_name,
            channel=channel)
        files[manifest_name] = file_url
    if filename:
        file_url = files.get(filename, None)
        if file_url is None:
            raise EntityNotFound(entity_id, filename)
        if read_file:
            data = self._get(file_url)
            return data.text
        else:
            return file_url
    else:
        return files