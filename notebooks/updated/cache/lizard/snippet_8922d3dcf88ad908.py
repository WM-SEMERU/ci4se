def get_table_from_csv(filename='ssg_report_aarons_returns.csv', delimiter=
    ',', dos=False):
    table = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f, dialect='excel', delimiter=delimiter)
        for row in reader:
            table += [row]
    if not dos:
        return table
    return dos_from_table(table)