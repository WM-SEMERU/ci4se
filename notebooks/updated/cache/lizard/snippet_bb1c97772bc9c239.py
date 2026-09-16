def write_csv_line(mol, csv_writer, options):
    status_field = options.status_field
    line = []
    id = mol.GetProp('id')
    if id is not None:
        line.append(id)
    else:
        line.append('n/a')
    line.append(mol.GetProp(status_field))
    queryList = mol.properties.keys()
    for queryLabel in queryList:
        line.append(mol.properties[queryLabel])
    csv_writer.writerow(line)