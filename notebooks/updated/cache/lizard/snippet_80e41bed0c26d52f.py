def tarfile_extract(fileobj, dest_path):
    tar = tarfile.open(mode='r|', fileobj=fileobj, bufsize=pipebuf.
        PIPE_BUF_BYTES)
    dest_path = os.path.realpath(dest_path)
    extracted_files = []
    for member in tar:
        assert not member.name.startswith('/')
        relpath = os.path.join(dest_path, member.name)
        if member.issym():
            target_path = os.path.join(dest_path, member.name)
            try:
                os.symlink(member.linkname, target_path)
            except OSError as e:
                if e.errno == errno.EEXIST:
                    os.remove(target_path)
                    os.symlink(member.linkname, target_path)
                else:
                    raise
            continue
        if member.isreg() and member.size >= pipebuf.PIPE_BUF_BYTES:
            cat_extract(tar, member, relpath)
        else:
            tar.extract(member, path=dest_path)
        filename = os.path.realpath(relpath)
        extracted_files.append(filename)
        if len(extracted_files) > 1000:
            _fsync_files(extracted_files)
            del extracted_files[:]
    tar.close()
    _fsync_files(extracted_files)