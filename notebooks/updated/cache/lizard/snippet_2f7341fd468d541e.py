def getCSVReader(data, reader_type=csv.DictReader):
    f = StringIO(data[:-4])
    return reader_type(f)