def call(self, command, *args):
    return self.rpc.call(str(command), *args)