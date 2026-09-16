def getdict(source):
    std_dict = {}
    for var, val in source.iteritems():
        std_dict[var] = source[var]
    return std_dict