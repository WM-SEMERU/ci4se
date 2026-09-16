def _attach(cls, iface_id, vm_id):
    oper = cls.call('hosting.vm.iface_attach', vm_id, iface_id)
    return oper