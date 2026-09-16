def generate(self, cache_root):
    generator_cwd = os.path.join(cache_root, 'generated', self.vlnv.
        sanitized_name)
    generator_input_file = os.path.join(generator_cwd, self.name + '_input.yml'
        )
    logger.info('Generating ' + str(self.vlnv))
    if not os.path.exists(generator_cwd):
        os.makedirs(generator_cwd)
    with open(generator_input_file, 'w') as f:
        f.write(yaml.dump(self.generator_input))
    args = [os.path.join(os.path.abspath(self.generator.root), self.
        generator.command), generator_input_file]
    if self.generator.interpreter:
        args[0:0] = [self.generator.interpreter]
    Launcher(args[0], args[1:], cwd=generator_cwd).run()
    cores = []
    logger.debug('Looking for generated cores in ' + generator_cwd)
    for root, dirs, files in os.walk(generator_cwd):
        for f in files:
            if f.endswith('.core'):
                try:
                    cores.append(Core(os.path.join(root, f)))
                except SyntaxError as e:
                    w = ('Failed to parse generated core file ' + f + ': ' +
                        e.msg)
                    raise RuntimeError(w)
    logger.debug('Found ' + ', '.join(str(c.name) for c in cores))
    return cores