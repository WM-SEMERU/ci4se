def fill_urls(self):
    protocol = self.dcnm_protocol
    self._org_url = '%s://%s/rest/auto-config/organizations' % (protocol,
        self._ip)
    self._create_network_url = '%s://%s/' % (protocol, self._ip
        ) + 'rest/auto-config/organizations/%s/partitions/%s/networks'
    self.host_protocol_url = '%s://%s/' % (protocol, self._ip)
    self._create_network_url = self._build_url(
        'rest/auto-config/organizations/%s/partitions/%s/networks')
    self._cfg_profile_list_url = '%s://%s/rest/auto-config/profiles' % (
        protocol, self._ip)
    self._cfg_profile_get_url = self._cfg_profile_list_url + '/%s'
    self._global_settings_url = self._build_url('rest/auto-config/settings')
    self._create_part_url = self._build_url(
        'rest/auto-config/organizations/%s/partitions')
    self._update_part_url = self._build_url(
        'rest/auto-config/organizations/%s/partitions/%s')
    self._del_org_url = self._build_url('rest/auto-config/organizations/%s')
    self._del_part = self._build_url(
        'rest/auto-config/organizations/%s/partitions/%s')
    self._network_url = self._build_url(
        'rest/auto-config/organizations/%s/partitions/%s/networks/segment/%s')
    self._network_mob_url = self._build_url(
        'rest/auto-config/organizations/%s/partitions/%s/networks/vlan/%s/mobility-domain/%s'
        )
    self._segmentid_ranges_url = self._build_url(
        'rest/settings/segmentid-ranges')
    self._login_url = self._build_url('rest/logon')
    self._logout_url = self._build_url('rest/logout')