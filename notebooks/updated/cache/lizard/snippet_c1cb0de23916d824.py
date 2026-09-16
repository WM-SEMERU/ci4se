def convert_args(self, command, args):
    for wanted, arg in zip(command.argtypes(), args):
        wanted = wanted.type_
        if wanted == 'const':
            try:
                yield to_int(arg)
            except:
                if arg in self.processor.constants:
                    yield self.processor.constants[arg]
                else:
                    yield arg
        if wanted == 'register':
            yield self.register_indices[arg]