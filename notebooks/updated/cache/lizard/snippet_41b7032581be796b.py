def string_list_file(cls, filename, values):
    fd = open(filename, 'w')
    for string in values:
        print >> fd, string
    fd.close()