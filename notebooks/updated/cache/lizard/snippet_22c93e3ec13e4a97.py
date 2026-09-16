def get_first_line(filepath, dialect):
    with open(filepath, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, dialect=dialect)
        for first_line in csvreader:
            break
    return first_line