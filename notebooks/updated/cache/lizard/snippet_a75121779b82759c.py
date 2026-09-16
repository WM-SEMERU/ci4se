def get_by_ip_hostname(self, ip_hostname):
    resources = self._client.get_all()
    resources_filtered = [x for x in resources if x['credentials'][
        'ip_hostname'] == ip_hostname]
    if resources_filtered:
        return resources_filtered[0]
    else:
        return None