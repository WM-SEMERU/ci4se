def list_folder(self, path):
    try:
        folder_contents = []
        for f in os.listdir(path):
            attr = paramiko.SFTPAttributes.from_stat(os.stat(os.path.join(
                path, f)))
            attr.filename = f
            folder_contents.append(attr)
        return folder_contents
    except OSError as e:
        return SFTPServer.convert_errno(e.errno)