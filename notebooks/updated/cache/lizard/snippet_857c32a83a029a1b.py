def populate_entries(self):
    try:
        with open(self.hosts_path, 'r') as hosts_file:
            hosts_entries = [line for line in hosts_file]
            for hosts_entry in hosts_entries:
                entry_type = HostsEntry.get_entry_type(hosts_entry)
                if entry_type == 'comment':
                    hosts_entry = hosts_entry.replace('\r', '')
                    hosts_entry = hosts_entry.replace('\n', '')
                    self.entries.append(HostsEntry(entry_type='comment',
                        comment=hosts_entry))
                elif entry_type == 'blank':
                    self.entries.append(HostsEntry(entry_type='blank'))
                elif entry_type in ('ipv4', 'ipv6'):
                    chunked_entry = hosts_entry.split()
                    stripped_name_list = [name.strip() for name in
                        chunked_entry[1:]]
                    self.entries.append(HostsEntry(entry_type=entry_type,
                        address=chunked_entry[0].strip(), names=
                        stripped_name_list))
    except IOError:
        return {'result': 'failed', 'message': 'Cannot read: {0}.'.format(
            self.hosts_path)}