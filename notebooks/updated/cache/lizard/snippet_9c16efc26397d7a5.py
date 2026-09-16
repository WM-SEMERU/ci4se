def _add_cable_to_equipment_changes(network, line):
    network.results.equipment_changes = (network.results.equipment_changes.
        append(pd.DataFrame({'iteration_step': [0], 'change': ['added'],
        'equipment': [line.type.name], 'quantity': [1]}, index=[line])))