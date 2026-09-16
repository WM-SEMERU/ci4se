def list_nodes_full(kwargs=None, call=None):
    if call == 'action':
        raise SaltCloudSystemExit(
            'The list_nodes_full function must be called with -f or --function.'
            )
    machines = {}
    for machine in vb_list_machines():
        name = machine.get('name')
        if name:
            machines[name] = treat_machine_dict(machine)
            del machine['name']
    return machines