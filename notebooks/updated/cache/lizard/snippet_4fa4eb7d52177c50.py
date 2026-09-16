def do_debug(self, args, arguments):
    filename = path_expand('~/.cloudmesh/cmd3.yaml')
    config = ConfigDict(filename=filename)
    if arguments['on']:
        self.set_debug(True)
    elif arguments['off']:
        self.set_debug(False)