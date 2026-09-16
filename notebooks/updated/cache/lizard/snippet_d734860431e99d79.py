def detect(self, root_device='/'):
    root = Device(None, [], None, '', [])
    device_nodes = dict(map(self._device_node, self._mounter.
        get_all_handleable()))
    for node in device_nodes.values():
        device_nodes.get(node.root, root).branches.append(node)
    device_nodes['/'] = root
    for node in device_nodes.values():
        node.branches.sort(key=lambda node: node.label)
    return device_nodes[root_device]