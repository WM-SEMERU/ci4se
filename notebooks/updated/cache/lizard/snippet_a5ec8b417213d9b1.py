def get_connection(self):
    if self.sniffer_timeout:
        if time.time() >= self.last_sniff + self.sniffer_timeout:
            self.sniff_hosts()
    return self.connection_pool.get_connection()