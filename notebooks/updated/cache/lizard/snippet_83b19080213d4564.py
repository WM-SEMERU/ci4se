def convert_destination_to_id(destination_node, destination_port, nodes):
    device_id = None
    device_name = None
    port_id = None
    if destination_node != 'NIO':
        for node in nodes:
            if destination_node == node['properties']['name']:
                device_id = node['id']
                device_name = destination_node
                for port in node['ports']:
                    if destination_port == port['name']:
                        port_id = port['id']
                        break
                break
    else:
        for node in nodes:
            if node['type'] == 'Cloud':
                for port in node['ports']:
                    if destination_port.lower() == port['name'].lower():
                        device_id = node['id']
                        device_name = node['properties']['name']
                        port_id = port['id']
                        break
    info = {'id': device_id, 'name': device_name, 'pid': port_id}
    return info