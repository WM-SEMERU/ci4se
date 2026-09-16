def rst(filename):
    content = open(filename).read()
    return re.sub('\\.\\.\\s? code-block::\\s*(\\w|\\+)+', '::', content)