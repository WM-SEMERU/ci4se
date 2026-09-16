def create_tomodir(self, directory):
    pwd = os.getcwd()
    if not os.path.isdir(directory):
        os.makedirs(directory)
    os.chdir(directory)
    directories = 'config', 'exe', 'grid', 'mod', 'mod/pot', 'mod/sens', 'rho'
    for directory in directories:
        if not os.path.isdir(directory):
            os.makedirs(directory)
    os.chdir(pwd)