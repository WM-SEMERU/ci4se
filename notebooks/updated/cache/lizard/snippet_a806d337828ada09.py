def generate(self, format, path=None, **environmentOptions):
    import warnings
    if format is None:
        raise ValueError('The format must be defined when generating.')
    elif not isinstance(format, basestring):
        raise TypeError('The format must be defined as a string.')
    env = {}
    for key, value in environmentOptions.items():
        valid = self._isValidGenerateEnvironmentOption(key)
        if not valid:
            warnings.warn(
                'The %s argument is not supported in this environment.' %
                key, UserWarning)
        env[key] = value
    environmentOptions = env
    ext = self.generateFormatToExtension(format, '.' + format)
    if path is None and self.path is None:
        raise IOError(
            'The file cannot be generated because an output path was not defined.'
            )
    elif path is None:
        path = os.path.splitext(self.path)[0]
        path += ext
    elif os.path.isdir(path):
        if self.path is None:
            raise IOError(
                'The file cannot be generated because the file does not have a path.'
                )
        fileName = os.path.basename(self.path)
        fileName += ext
        path = os.path.join(path, fileName)
    path = normalizers.normalizeFilePath(path)
    return self._generate(format=format, path=path, environmentOptions=
        environmentOptions)