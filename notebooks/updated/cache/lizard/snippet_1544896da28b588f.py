def create_package(project, name, sourcefolder=None):
    if sourcefolder is None:
        sourcefolder = project.root
    packages = name.split('.')
    parent = sourcefolder
    for package in packages[:-1]:
        parent = parent.get_child(package)
    made_packages = parent.create_folder(packages[-1])
    made_packages.create_file('__init__.py')
    return made_packages