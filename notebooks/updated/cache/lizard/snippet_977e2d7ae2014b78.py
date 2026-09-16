def uifile(self):
    output = ''
    if zipfile.is_zipfile(self.source()):
        zfile = zipfile.ZipFile(self.source(), 'r')
        if 'properties.ui' in zfile.namelist():
            tempdir = tempfile.gettempdir()
            output = os.path.join(tempdir, '{0}_properties.ui'.format(self.
                name()))
            f = open(output, 'w')
            f.write(zfile.read('properties.ui'))
            f.close()
        zfile.close()
    else:
        uifile = os.path.join(os.path.dirname(self.source()), 'properties.ui')
        if os.path.exists(uifile):
            output = uifile
    return output