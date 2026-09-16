def GetRootFileEntry(self):
    if platform.system() == 'Windows':
        location = os.getcwd()
        location, _, _ = location.partition('\\')
        location = '{0:s}\\'.format(location)
    else:
        location = '/'
    if not os.path.exists(location):
        return None
    path_spec = os_path_spec.OSPathSpec(location=location)
    return self.GetFileEntryByPathSpec(path_spec)