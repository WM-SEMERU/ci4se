def provision(self, vm_name=None, provision_with=None):
    prov_with_arg = None if provision_with is None else '--provision-with'
    providers_arg = None if provision_with is None else ','.join(provision_with
        )
    self._call_vagrant_command(['provision', vm_name, prov_with_arg,
        providers_arg])