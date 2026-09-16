def _import(self, record_key, record_data, overwrite=True, last_modified=
    0.0, **kwargs):
    title = '%s._import' % self.__class__.__name__
    if not overwrite:
        if self.exists(record_key):
            return False
    import sys
    record_max = self.fields.metadata['record_max_bytes']
    record_size = sys.getsizeof(record_data)
    error_prefix = '%s(record_key="%s", record_data=b"...")' % (title,
        record_key)
    if record_size > record_max:
        raise ValueError('%s exceeds maximum record data size of %s bytes.' %
            (error_prefix, record_max))
    upload_kwargs = {'f': record_data, 'path': '/%s' % record_key, 'mute':
        True, 'mode': self.objects.WriteMode.overwrite}
    import re
    if re.search('\\.drep$', record_key):
        from labpack.records.time import labDT
        drep_time = labDT.fromEpoch(1)
        upload_kwargs['client_modified'] = drep_time
    elif last_modified:
        from labpack.records.time import labDT
        mod_time = labDT.fromEpoch(last_modified)
        upload_kwargs['client_modified'] = mod_time
    try:
        self.dropbox.files_upload(**upload_kwargs)
    except:
        raise DropboxConnectionError(title)
    return True