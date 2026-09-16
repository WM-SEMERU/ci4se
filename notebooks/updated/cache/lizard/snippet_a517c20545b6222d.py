def create_reader_of_type(type_name):
    readers = available_readers()
    if type_name not in readers.keys():
        raise UnknownReaderException('Unknown reader: %s' % (type_name,))
    return readers[type_name]()