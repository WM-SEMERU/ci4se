def backup_restore(cls, block_id, impl, working_dir):
    backup_dir = config.get_backups_directory(impl, working_dir)
    backup_paths = cls.get_backup_paths(block_id, impl, working_dir)
    for p in backup_paths:
        assert os.path.exists(p), 'No such backup file: {}'.format(p)
    for p in cls.get_state_paths(impl, working_dir):
        pbase = os.path.basename(p)
        backup_path = os.path.join(backup_dir, pbase + '.bak.{}'.format(
            block_id))
        log.debug("Restoring '{}' to '{}'".format(backup_path, p))
        shutil.copy(backup_path, p)
    return True