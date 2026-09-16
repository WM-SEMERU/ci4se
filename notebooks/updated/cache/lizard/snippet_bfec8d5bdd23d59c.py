def _backup_dir_item(self, dir_path, process_bar):
    self.path_helper.set_src_filepath(dir_path)
    if self.path_helper.abs_src_filepath is None:
        self.total_errored_items += 1
        log.info("Can't backup %r", dir_path)
    if dir_path.is_symlink:
        self.summary('TODO Symlink: %s' % dir_path)
        return
    if dir_path.resolve_error is not None:
        self.summary('TODO resolve error: %s' % dir_path.resolve_error)
        pprint_path(dir_path)
        return
    if dir_path.different_path:
        self.summary('TODO different path:')
        pprint_path(dir_path)
        return
    if dir_path.is_dir:
        self.summary('TODO dir: %s' % dir_path)
    elif dir_path.is_file:
        file_backup = FileBackup(dir_path, self.path_helper, self.backup_run)
        old_backup_entry = self.fast_compare(dir_path)
        if old_backup_entry is not None:
            file_backup.fast_deduplication_backup(old_backup_entry, process_bar
                )
        else:
            file_backup.deduplication_backup(process_bar)
        assert file_backup.fast_backup is not None, dir_path.path
        assert file_backup.file_linked is not None, dir_path.path
        file_size = dir_path.stat.st_size
        if file_backup.file_linked:
            self.total_file_link_count += 1
            self.total_stined_bytes += file_size
        else:
            self.total_new_file_count += 1
            self.total_new_bytes += file_size
        if file_backup.fast_backup:
            self.total_fast_backup += 1
    else:
        self.summary('TODO:' % dir_path)
        pprint_path(dir_path)