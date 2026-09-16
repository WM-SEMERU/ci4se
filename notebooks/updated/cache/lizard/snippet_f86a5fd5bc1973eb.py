def get_older_backup(self, encrypted=None, compressed=None, content_type=
    None, database=None, servername=None):
    files = self.list_backups(encrypted=encrypted, compressed=compressed,
        content_type=content_type, database=database, servername=servername)
    if not files:
        raise FileNotFound("There's no backup file available.")
    return min(files, key=utils.filename_to_date)