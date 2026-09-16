def get_port_name_from_id(node_id, port_id, nodes):
    port_name = ''
    for node in nodes:
        if node['id'] == node_id:
            for port in node['ports']:
                if port['id'] == port_id:
                    port_name = port['name']
                    break
    return port_name