def check(self, url_data):
    host = url_data.urlparts[1]
    if host in self.checked_hosts:
        return
    self.checked_hosts.add(host)
    cert = url_data.ssl_cert
    config = url_data.aggregate.config
    if cert and 'notAfter' in cert:
        self.check_ssl_valid_date(url_data, cert)
    elif config['sslverify']:
        msg = _('certificate did not include "notAfter" information')
        url_data.add_warning(msg)
    else:
        msg = _('SSL verification is disabled; enable the sslverify option')
        url_data.add_warning(msg)