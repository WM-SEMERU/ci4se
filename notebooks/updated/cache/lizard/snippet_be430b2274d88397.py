def _get_log_file(self, handler):
    if 'file_name_pattern' not in handler:
        filename = '%Y-%m-%d-%H-%M-%S-{name}.pcap'
    else:
        filename = handler['file_name_pattern']
    log_file = handler['log_dir']
    if 'path' in handler:
        log_file = os.path.join(log_file, handler['path'], filename)
    else:
        log_file = os.path.join(log_file, filename)
    log_file = time.strftime(log_file, time.gmtime())
    log_file = log_file.format(**handler)
    return log_file