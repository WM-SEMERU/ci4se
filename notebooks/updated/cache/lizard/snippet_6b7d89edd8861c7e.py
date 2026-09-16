def sync(self):
    detected_ip = self.detector.detect()
    if detected_ip is None:
        LOG.debug("Couldn't detect the current IP using detector %r", self.
            detector.names()[-1])
    elif self.dns.detect() != detected_ip:
        LOG.info("%s: dns IP '%s' does not match detected IP '%s', updating",
            self.updater.hostname, self.dns.get_current_value(), detected_ip)
        self.status = self.updater.update(detected_ip)
        self.plugins.after_remote_ip_update(detected_ip, self.status)
    else:
        self.status = 0
        LOG.debug("%s: nothing to do, dns '%s' equals detection '%s'", self
            .updater.hostname, self.dns.get_current_value(), self.detector.
            get_current_value())