def create_partition(self, org_name, part_name, dci_id, vrf_prof,
    service_node_ip=None, desc=None):
    desc = desc or org_name
    res = self._create_or_update_partition(org_name, part_name, desc,
        dci_id=dci_id, service_node_ip=service_node_ip, vrf_prof=vrf_prof)
    if res and res.status_code in self._resp_ok:
        LOG.debug('Created %s partition in DCNM.', part_name)
    else:
        LOG.error(
            'Failed to create %(part)s partition in DCNM.Response: %(res)s',
            {'part': part_name, 'res': res})
        raise dexc.DfaClientRequestFailed(reason=self._failure_msg(res))