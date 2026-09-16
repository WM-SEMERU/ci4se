def process(self):
    client = self._get_client_by_hostname(self.host)
    self._await_flow(client, self.flow_id)
    collected_flow_data = self._download_files(client, self.flow_id)
    if collected_flow_data:
        print('{0:s}: Downloaded: {1:s}'.format(self.flow_id,
            collected_flow_data))
        fqdn = client.data.os_info.fqdn.lower()
        self.state.output.append((fqdn, collected_flow_data))