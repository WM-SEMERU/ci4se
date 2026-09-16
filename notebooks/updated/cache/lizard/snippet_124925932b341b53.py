def generate_csv(in_dir, out):
    writer = UnicodeWriter(open(out, 'wb'), delimiter=';')
    writer.writerow(('Reference ID', 'Created', 'Origin', 'Subject'))
    for cable in cables_from_source(in_dir):
        writer.writerow((cable.reference_id, cable.created, cable.origin,
            titlefy(cable.subject)))