def compute_file_hashes(file_path, hashes=frozenset(['md5'])):
    if not os.path.exists(file_path):
        logging.warning('%s does not exist' % file_path)
        return
    else:
        logging.debug('Computing [%s] hashes for file [%s]' % (','.join(
            hashes), file_path))
    try:
        with open(file_path, 'rb') as fd:
            return compute_hashes(fd, hashes)
    except (IOError, OSError) as e:
        logging.warning('Error while calculating digest(s) for file %s: %s' %
            (file_path, str(e)))
        raise