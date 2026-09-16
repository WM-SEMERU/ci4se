def update_hosts_file(self, ip, entry):
    log = logging.getLogger(self.cls_logger + '.update_hosts_file')
    if get_os() in ['Linux', 'Darwin']:
        update_hosts_file_linux(ip=ip, entry=entry)
    elif get_os() == 'Windows':
        update_hosts_file_windows(ip=ip, entry=entry)
    else:
        log.warn('OS detected was not Windows nor Linux')