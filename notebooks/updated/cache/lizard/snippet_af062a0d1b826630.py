def delete(sld, tld, nameserver):
    opts = salt.utils.namecheap.get_opts('namecheap.domains.ns.delete')
    opts['SLD'] = sld
    opts['TLD'] = tld
    opts['Nameserver'] = nameserver
    response_xml = salt.utils.namecheap.post_request(opts)
    if response_xml is None:
        return False
    domainnsdeleteresult = response_xml.getElementsByTagName(
        'DomainNSDeleteResult')[0]
    return salt.utils.namecheap.string_to_value(domainnsdeleteresult.
        getAttribute('IsSuccess'))