def _parse_domain_caps(caps):
    result = {'emulator': caps.find('path').text if caps.find('path') is not
        None else None, 'domain': caps.find('domain').text if caps.find(
        'domain') is not None else None, 'machine': caps.find('machine').
        text if caps.find('machine') is not None else None, 'arch': caps.
        find('arch').text if caps.find('arch') is not None else None}
    for child in caps:
        if child.tag == 'vcpu' and child.get('max'):
            result['max_vcpus'] = int(child.get('max'))
        elif child.tag == 'iothreads':
            result['iothreads'] = child.get('supported') == 'yes'
        elif child.tag == 'os':
            result['os'] = {}
            loader_node = child.find('loader')
            if loader_node is not None and loader_node.get('supported'
                ) == 'yes':
                loader = _parse_caps_loader(loader_node)
                result['os']['loader'] = loader
        elif child.tag == 'cpu':
            cpu = _parse_caps_cpu(child)
            if cpu:
                result['cpu'] = cpu
        elif child.tag == 'devices':
            devices = _parse_caps_devices_features(child)
            if devices:
                result['devices'] = devices
        elif child.tag == 'features':
            features = _parse_caps_devices_features(child)
            if features:
                result['features'] = features
    return result