def pci_contents(self, use_dict=None, as_class=dict):
    if _debug:
        PCI._debug('pci_contents use_dict=%r as_class=%r', use_dict, as_class)
    if use_dict is None:
        use_dict = as_class()
    for k, v in (('user_data', self.pduUserData), ('source', self.pduSource
        ), ('destination', self.pduDestination)):
        if _debug:
            PCI._debug('    - %r: %r', k, v)
        if v is None:
            continue
        if hasattr(v, 'dict_contents'):
            v = v.dict_contents(as_class=as_class)
        use_dict.__setitem__(k, v)
    return use_dict