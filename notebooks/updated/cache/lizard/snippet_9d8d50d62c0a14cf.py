def _update_partition_srvc_node_ip(self, tenant_name, srvc_ip, vrf_prof=
    None, part_name=None):
    self.dcnm_obj.update_project(tenant_name, part_name, service_node_ip=
        srvc_ip, vrf_prof=vrf_prof, desc='Service Partition')