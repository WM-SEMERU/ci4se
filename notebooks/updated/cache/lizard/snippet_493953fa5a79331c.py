def run(self):
    install.run(self)
    spath = os.path.join(self.install_scripts, 'pygubu')
    for ext in ('.py', '.pyw'):
        filename = spath + ext
        if os.path.exists(filename):
            os.remove(filename)
    if platform.system() == 'Windows':
        spath = os.path.join(self.install_scripts, 'pygubu-designer.bat')
        if os.path.exists(spath):
            os.remove(spath)