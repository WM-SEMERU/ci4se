def download(self, obj, directory, structure=True):
    if not os.path.isdir(directory):
        raise exc.FolderNotFound("The directory '%s' does not exist." %
            directory)
    obj_name = utils.get_name(obj)
    path, fname = os.path.split(obj_name)
    if structure:
        fullpath = os.path.join(directory, path)
        if not os.path.exists(fullpath):
            os.makedirs(fullpath)
        target = os.path.join(fullpath, fname)
    else:
        target = os.path.join(directory, fname)
    with open(target, 'wb') as dl:
        content = self.fetch(obj)
        try:
            dl.write(content)
        except UnicodeEncodeError:
            encoding = pyrax.get_encoding()
            dl.write(content.encode(encoding))