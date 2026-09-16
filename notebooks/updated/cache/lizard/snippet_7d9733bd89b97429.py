def handle_units(changeset):
    units, records = {}, {}
    for service_name, service in sorted(changeset.bundle['services'].items()):
        for i in range(service.get('num_units', 0)):
            record_id = 'addUnit-{}'.format(changeset.next_action())
            unit_name = '{}/{}'.format(service_name, i)
            records[record_id] = {'id': record_id, 'method': 'addUnit',
                'args': ['${}'.format(changeset.services_added[service_name
                ]), None], 'requires': [changeset.services_added[service_name]]
                }
            units[unit_name] = {'record': record_id, 'service':
                service_name, 'unit': i}
    _handle_units_placement(changeset, units, records)