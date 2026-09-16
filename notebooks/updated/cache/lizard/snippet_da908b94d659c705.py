def read_csv(filename, delimiter=CSV_DELIMITER):
    with open(filename, 'r') as file:
        return list(csv.reader(file, delimiter=delimiter))