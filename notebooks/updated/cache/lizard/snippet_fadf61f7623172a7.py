def scan_file(self, src_file):
    self.logger.info('start scanning file {} for proxy list...'.format(
        src_file))
    with open(src_file, 'r') as fin:
        proxies = json.load(fin)
    for protocol in proxies.keys():
        for proxy in proxies[protocol]:
            self.proxy_queue.put({'addr': proxy['addr'], 'protocol': protocol})