def lookup(domain):
    xml = domain.XMLDesc(0)
    element = etree.fromstring(xml)
    subelm = element.find('.//interface[@type="network"]')
    if subelm is not None:
        network = subelm.find('.//source').get('network')
        hypervisor = domain.connect()
        return hypervisor.networkLookupByName(network)
    return None