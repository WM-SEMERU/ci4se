def put_path(self, path):
    if self.is_package(path):
        logger.debug('PYTHON PACKAGE: {}'.format(path))
        self.python_paths.append(path.parent)
        site.addsitedir(str(path.parent))
        xbmdirs = self.get_directories_with_extensions(path, self.
            icon_extensions)
        self.xbmlang_paths.extend(xbmdirs)
        return
    if self.has_next(path.glob('*.' + self.MEL)):
        logger.debug('MEL: {}'.format(str(path)))
        self.script_paths.append(path)
    if self.has_next(path.glob('*.' + self.PYTHON)):
        logger.debug('PYTHONPATH: {}'.format(str(path)))
        self.python_paths.append(path)
        site.addsitedir(str(path))
    if self.PLUGIN in list(path.iterdir()):
        logger.debug('PLUG-IN: {}'.format(str(path)))
        self.plug_in_paths.append(path)
    for ext in self.icon_extensions:
        if self.has_next(path.glob('*.' + ext)):
            logger.debug('XBM: {}.'.format(str(path)))
            self.xbmlang_paths.append(path)
            break