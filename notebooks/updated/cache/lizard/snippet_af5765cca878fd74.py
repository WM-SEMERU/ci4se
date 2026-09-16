def dump_config(self):
    yaml_content = self.get_merged_config()
    print('YAML Configuration\n%s\n' % yaml_content.read())
    try:
        self.load()
        print('Python Configuration\n%s\n' % pretty(self.yamldocs))
    except ConfigError:
        sys.stderr.write(
            'config parse error. try running with --logfile=/dev/tty\n')
        raise