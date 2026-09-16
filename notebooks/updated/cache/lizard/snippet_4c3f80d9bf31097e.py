def to_csv(self, fileobj=sys.stdout):
    openclose = is_string(fileobj)
    if openclose:
        fileobj = open(fileobj, 'w')
    for idx, section in enumerate(self.sections):
        fileobj.write(section.to_csvline(with_header=idx == 0))
    fileobj.flush()
    if openclose:
        fileobj.close()