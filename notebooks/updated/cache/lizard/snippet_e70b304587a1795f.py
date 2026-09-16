def get_lib(self, arch='x86', native=False):
    if self.sdk_version == 'v7.0A':
        if arch == 'x86':
            arch = ''
        lib = os.path.join(self.sdk_dir, 'lib', arch)
        if os.path.isdir(lib):
            logging.info(_('using lib: %s'), lib)
            return [lib]
        logging.debug(_('lib not found: %s'), lib)
        return []
    if self.sdk_version == 'v8.1':
        if native:
            extra = os.path.join('winv6.3', 'km')
        else:
            extra = os.path.join('winv6.3', 'um')
        lib = os.path.join(self.sdk_dir, 'lib', extra, arch)
        if os.path.isdir(lib):
            logging.info(_('using lib: %s'), lib)
            return [lib]
        logging.debug(_('lib not found: %s'), lib)
        return []
    if self.sdk_version == 'v10.0':
        dirs = []
        extra = os.path.join('lib', '10.0.10240.0')
        for mode in ['um', 'ucrt']:
            lib = os.path.join(self.sdk_dir, extra, mode, arch)
            if os.path.isdir(lib):
                logging.info(_('using lib: %s'), lib)
                dirs.append(lib)
            else:
                logging.debug(_('lib not found: %s'), lib)
        return dirs
    message = 'unknown sdk version: {}'.format(self.sdk_version)
    raise RuntimeError(message)