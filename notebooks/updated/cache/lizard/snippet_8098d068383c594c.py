def duplicate_node(self, node, x, y, z):
    if node.status != 'stopped' and not node.is_always_running():
        raise aiohttp.web.HTTPConflict(text=
            'Cannot duplicate node data while the node is running')
    data = copy.deepcopy(node.__json__(topology_dump=True))
    for unique_property in ('node_id', 'name', 'mac_addr', 'mac_address',
        'compute_id', 'application_id', 'dynamips_id'):
        data.pop(unique_property, None)
        if 'properties' in data:
            data['properties'].pop(unique_property, None)
    node_type = data.pop('node_type')
    data['x'] = x
    data['y'] = y
    data['z'] = z
    new_node_uuid = str(uuid.uuid4())
    new_node = yield from self.add_node(node.compute, node.name,
        new_node_uuid, node_type=node_type, **data)
    try:
        yield from node.post('/duplicate', timeout=None, data={
            'destination_node_id': new_node_uuid})
    except aiohttp.web.HTTPNotFound as e:
        yield from self.delete_node(new_node_uuid)
        raise aiohttp.web.HTTPConflict(text=
            'This node type cannot be duplicated')
    except aiohttp.web.HTTPConflict as e:
        yield from self.delete_node(new_node_uuid)
        raise e
    return new_node