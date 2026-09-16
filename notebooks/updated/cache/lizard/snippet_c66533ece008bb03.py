def dest_ports(self):
    start_port = self.blacklist.get('BlacklistEntryDestinationPort')
    if start_port is not None:
        return '{}-{}'.format(start_port, self.blacklist.get(
            'BlacklistEntryDestinationPortRange'))
    return 'ANY'