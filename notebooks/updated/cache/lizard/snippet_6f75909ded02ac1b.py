def get_item_sh(self, item):
    sh_fields = {}
    if 'member' in item:
        identity = self.get_sh_identity(item['member'])
    elif 'event_hosts' in item:
        identity = self.get_sh_identity(item['event_hosts'][0])
    else:
        return sh_fields
    created = unixtime_to_datetime(item['created'] / 1000)
    sh_fields = self.get_item_sh_fields(identity, created)
    return sh_fields