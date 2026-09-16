def recall_checksum(self, cache_file):
    checksum_file = '%s.txt' % cache_file
    try:
        with open(checksum_file) as handle:
            contents = handle.read()
        return contents.strip()
    except IOError as e:
        if e.errno == errno.ENOENT:
            return None
        else:
            raise