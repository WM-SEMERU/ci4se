def integer_list_file(cls, filename, values, bits=None):
    fd = open(filename, 'w')
    for integer in values:
        print >> fd, cls.integer(integer, bits)
    fd.close()