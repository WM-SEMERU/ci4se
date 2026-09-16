def _dot1q_headers_size(layer):
    vlan_headers_size = 0
    under_layer = layer
    while under_layer and isinstance(under_layer, Dot1Q):
        vlan_headers_size += LLDPDU.DOT1Q_HEADER_LEN
        under_layer = under_layer.underlayer
    return vlan_headers_size, under_layer