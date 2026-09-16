def to_didl_string(*args):
    didl = XML.Element('DIDL-Lite', {'xmlns':
        'urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/', 'xmlns:dc':
        'http://purl.org/dc/elements/1.1/', 'xmlns:upnp':
        'urn:schemas-upnp-org:metadata-1-0/upnp/', 'xmlns:r':
        'urn:schemas-rinconnetworks-com:metadata-1-0/'})
    for arg in args:
        didl.append(arg.to_element())
    if sys.version_info[0] == 2:
        return XML.tostring(didl)
    else:
        return XML.tostring(didl, encoding='unicode')