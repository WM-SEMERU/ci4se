def do_version(self, args):
    Console.ok('cmd3: {:}'.format(str(cmd3.__version__)))
    Console.ok('cloudmesh_base: {:}'.format(str(cloudmesh_base.__version__)))
    python_version, pip_version = get_python()
    Console.ok('python: {:}'.format(str(python_version)))
    Console.ok('pip: {:}'.format(str(pip_version)))
    check_python()