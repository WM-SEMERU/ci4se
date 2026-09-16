def read_to_file(library, session, filename, count):
    return_count = ViUInt32()
    ret = library.viReadToFile(session, filename, count, return_count)
    return return_count, ret