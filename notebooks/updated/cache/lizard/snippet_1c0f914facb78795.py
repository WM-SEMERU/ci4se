def is_file_ignored(opts, fname):
    if opts['file_ignore_regex']:
        for regex in opts['file_ignore_regex']:
            if re.search(regex, fname):
                log.debug('File matching file_ignore_regex. Skipping: %s',
                    fname)
                return True
    if opts['file_ignore_glob']:
        for glob in opts['file_ignore_glob']:
            if fnmatch.fnmatch(fname, glob):
                log.debug('File matching file_ignore_glob. Skipping: %s', fname
                    )
                return True
    return False