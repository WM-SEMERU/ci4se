def file_update_file(self, quick_key, file_extension=None, filename=None,
    description=None, mtime=None, privacy=None, timezone=None):
    return self.request('file/update', QueryParams({'quick_key': quick_key,
        'file_extension': file_extension, 'filename': filename,
        'description': description, 'mtime': mtime, 'privacy': privacy,
        'timezone': timezone}))