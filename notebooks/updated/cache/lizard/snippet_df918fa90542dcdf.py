def _query(self, filename):
    log.Info('Querying size of %s' % filename)
    from jottalib.JFS import JFSNotFoundError, JFSIncompleteFile
    remote_path = posixpath.join(self.folder.path, filename)
    try:
        remote_file = self.client.getObject(remote_path)
    except JFSNotFoundError:
        return {'size': -1}
    return {'size': remote_file.size}