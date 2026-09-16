def k8s_ports_to_metadata_ports(k8s_ports):
    ports = []
    for k8s_port in k8s_ports:
        if k8s_port.protocol is not None:
            ports.append('%s/%s' % (k8s_port.port, k8s_port.protocol.lower()))
        else:
            ports.append(str(k8s_port.port))
    return ports