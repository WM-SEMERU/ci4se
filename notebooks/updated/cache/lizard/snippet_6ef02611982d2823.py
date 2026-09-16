def get_admins_from_django(homedir):
    return ['root@localhost']
    path = homedir + '/settings/basic.py'
    if not os.path.exists(path):
        path = homedir + '/settings.py'
    if not os.path.exists(path):
        return
    mod = compiler.parseFile(path)
    for node in mod.node.nodes:
        try:
            if node.asList()[0].name == 'ADMINS':
                return [it.nodes[1].value for it in node.asList()[1].asList()]
        except:
            pass