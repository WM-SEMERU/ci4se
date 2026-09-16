def preprocess_files(self, prefix):
    if prefix is None:
        return
    files = 'bin/yang2dsdl', 'man/man1/yang2dsdl.1', 'pyang/plugins/jsonxsl.py'
    regex = re.compile('^(.*)/usr/local(.*)$')
    for f in files:
        inf = open(f)
        cnt = inf.readlines()
        inf.close()
        ouf = open(f, 'w')
        for line in cnt:
            mo = regex.search(line)
            if mo is None:
                ouf.write(line)
            else:
                ouf.write(mo.group(1) + prefix + mo.group(2) + '\n')
        ouf.close()