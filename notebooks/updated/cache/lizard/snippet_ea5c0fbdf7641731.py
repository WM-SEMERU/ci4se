def _get_logger(self, handler):
    log_file = self._get_log_file(handler)
    if not os.path.isdir(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    handler['log_rot_time'] = time.gmtime()
    return pcap.open(log_file, mode='a')