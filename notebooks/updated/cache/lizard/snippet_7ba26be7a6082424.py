def _delete_partition(self, org_name, partition_name):
    url = self._del_part % (org_name, partition_name)
    return self._send_request('DELETE', url, '', 'partition')