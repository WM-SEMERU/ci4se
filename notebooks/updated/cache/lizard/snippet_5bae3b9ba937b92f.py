def retrieveVals(self):
    ntpinfo = NTPinfo()
    stats = ntpinfo.getPeerStats()
    if stats:
        if self.hasGraph('ntp_peer_stratum'):
            self.setGraphVal('ntp_peer_stratum', 'stratum', stats.get(
                'stratum'))
        if self.hasGraph('ntp_peer_stats'):
            self.setGraphVal('ntp_peer_stats', 'offset', stats.get('offset'))
            self.setGraphVal('ntp_peer_stats', 'delay', stats.get('delay'))
            self.setGraphVal('ntp_peer_stats', 'jitter', stats.get('jitter'))