def create_package(self, dirpath):
    dirpath = fixpath(dirpath)
    filepath = os.path.join(dirpath, '__coconut__.py')
    with openfile(filepath, 'w') as opened:
        writefile(opened, self.comp.getheader('__coconut__'))