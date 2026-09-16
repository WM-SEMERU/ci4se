def put(self, localpath, remotepath, callback=None, confirm=True):
    file_size = os.stat(localpath).st_size
    with open(localpath, 'rb') as fl:
        return self.putfo(fl, remotepath, file_size, callback, confirm)