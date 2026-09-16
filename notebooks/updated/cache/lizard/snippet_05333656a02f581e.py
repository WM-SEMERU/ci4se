def clean_old_backups(self, encrypted=None, compressed=None, content_type=
    None, database=None, servername=None, keep_number=None):
    if keep_number is None:
        keep_number = (settings.CLEANUP_KEEP if content_type == 'db' else
            settings.CLEANUP_KEEP_MEDIA)
    keep_filter = settings.CLEANUP_KEEP_FILTER
    files = self.list_backups(encrypted=encrypted, compressed=compressed,
        content_type=content_type, database=database, servername=servername)
    files = sorted(files, key=utils.filename_to_date, reverse=True)
    files_to_delete = [fi for i, fi in enumerate(files) if i >= keep_number]
    for filename in files_to_delete:
        if keep_filter(filename):
            continue
        self.delete_file(filename)