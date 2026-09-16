def handle_timeout(self, scan_id, host):
    self.add_scan_error(scan_id, host=host, name='Timeout', value=
        '{0} exec timeout.'.format(self.get_scanner_name()))