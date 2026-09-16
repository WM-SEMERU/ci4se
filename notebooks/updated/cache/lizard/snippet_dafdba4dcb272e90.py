def get_instances_in_role(self, role, state_filter=None):
    self._check_role_name(role)
    instances = []
    for instance in self._get_instances(self._group_name_for_role(role),
        state_filter):
        instances.append(Instance(instance.id, instance.dns_name, instance.
            private_dns_name, instance.private_ip_address))
    return instances