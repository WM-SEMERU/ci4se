def run(self):
    if sys.platform == 'linux' or sys.platform == 'linux2':
        libname = 'libfaketime.so.1'
        libnamemt = 'libfaketimeMT.so.1'
    elif sys.platform == 'darwin':
        libname = 'libfaketime.1.dylib'
        libnamemt = 'libfaketimeMT.1.dylib'
    else:
        sys.stderr.write('WARNING : libfaketime does not support platform {}\n'
            .format(sys.platform))
        sys.stderr.flush()
        return
    faketime_lib = join('faketime', libname)
    faketime_lib_mt = join('faketime', libnamemt)
    self.my_outputs = []
    setup_py_directory = dirname(realpath(__file__))
    faketime_directory = join(setup_py_directory, 'faketime')
    os.chdir(faketime_directory)
    if sys.platform == 'linux' or sys.platform == 'linux2':
        subprocess.check_call(['make'])
    else:
        os.chdir(setup_py_directory)
        if '10.12' in subprocess.check_output(['sw_vers', '-productVersion']
            ).decode('utf8'):
            self.copy_file(join('faketime', 'libfaketime.c.sierra'), join(
                'faketime', 'libfaketime.c'))
        os.chdir(faketime_directory)
        subprocess.check_call(['make', '-f', 'Makefile.OSX'])
    os.chdir(setup_py_directory)
    dest = join(self.install_purelib, dirname(faketime_lib))
    dest_mt = join(self.install_purelib, dirname(faketime_lib_mt))
    try:
        os.makedirs(dest)
    except OSError as e:
        if e.errno != 17:
            raise
    self.copy_file(faketime_lib, dest)
    if exists(faketime_lib_mt):
        self.copy_file(faketime_lib_mt, dest_mt)
    self.my_outputs.append(join(dest, libname))
    install.run(self)