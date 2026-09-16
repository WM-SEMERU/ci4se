def retrieve_config(element):
    if not etree.iselement(element):
        raise TypeError("argument 'element' must be Element not '{}'".
            format(type(element)))
    ret = etree.Element(config_tag, nsmap={'nc': nc_url})
    ret.extend(deepcopy(element.xpath('/nc:rpc-reply/nc:data/*', namespaces
        ={'nc': nc_url})))
    ret.extend(deepcopy(element.xpath('/nc:data/*', namespaces={'nc': nc_url}))
        )
    ret.extend(deepcopy(element.xpath('/nc:config/*', namespaces={'nc':
        nc_url})))
    ret.extend(deepcopy(element.xpath('/nc:rpc/nc:edit-config/nc:config/*',
        namespaces={'nc': nc_url})))
    ret.extend(deepcopy(element.xpath('/nc:edit-config/nc:config/*',
        namespaces={'nc': nc_url})))
    return ret