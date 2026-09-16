def create_conf_file(self):
    cmd_obj = self.distribution.get_command_obj('install')
    cmd_obj.ensure_finalized()
    data = []
    for d in ['purelib', 'platlib', 'lib', 'headers', 'scripts', 'data']:
        attr = 'install_%s' % d
        if cmd_obj.root:
            cutoff = len(cmd_obj.root)
            if cmd_obj.root.endswith(os.sep):
                cutoff -= 1
            val = getattr(cmd_obj, attr)[cutoff:]
        else:
            val = getattr(cmd_obj, attr)
        if attr == 'install_data':
            cdir = os.path.join(val, 'share', 'linkchecker')
            data.append('config_dir = %r' % cnormpath(cdir))
        elif attr == 'install_lib':
            if cmd_obj.root:
                _drive, tail = os.path.splitdrive(val)
                if tail.startswith(os.sep):
                    tail = tail[1:]
                self.install_lib = os.path.join(cmd_obj.root, tail)
            else:
                self.install_lib = val
        data.append('%s = %r' % (attr, cnormpath(val)))
    self.distribution.create_conf_file(data, directory=self.install_lib)
    return self.get_conf_output()