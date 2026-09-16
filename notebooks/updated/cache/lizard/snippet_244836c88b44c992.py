def download_file(self, regex, dest_dir):
    log = logging.getLogger(self.cls_logger + '.download_file')
    if not isinstance(regex, basestring):
        log.error('regex argument is not a string')
        return None
    if not isinstance(dest_dir, basestring):
        log.error('dest_dir argument is not a string')
        return None
    if not os.path.isdir(dest_dir):
        log.error('Directory not found on file system: %s', dest_dir)
        return None
    key = self.find_key(regex)
    if key is None:
        log.warn('Could not find a matching S3 key for: %s', regex)
        return None
    return self.__download_from_s3(key, dest_dir)