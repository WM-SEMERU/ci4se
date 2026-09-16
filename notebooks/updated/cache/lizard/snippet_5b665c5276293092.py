def command_init(self):
    self.parser = argparse.ArgumentParser(description=
        'Initialize a new metadata tree')
    self.options_utils()
    self.options = self.parser.parse_args(self.arguments[2:])
    for path in (self.options.paths or ['.']):
        root = os.path.abspath(os.path.join(path, '.fmf'))
        if os.path.exists(root):
            raise utils.FileError("{0} '{1}' already exists.".format(
                'Directory' if os.path.isdir(root) else 'File', root))
        os.makedirs(root)
        with open(os.path.join(root, 'version'), 'w') as version:
            version.write('{0}\n'.format(utils.VERSION))
        print("Metadata tree '{0}' successfully initialized.".format(root))