def delete_archive_dir(self):
    logger.debug('Deleting: ' + self.archive_dir)
    shutil.rmtree(self.archive_dir, True)