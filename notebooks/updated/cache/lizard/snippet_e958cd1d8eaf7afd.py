def register_file(name, member, path, digest='', conn=None):
    close = False
    if conn is None:
        close = True
        conn = init()
    conn.execute(
        'INSERT INTO files VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
        name, '{0}/{1}'.format(path, member.path), member.size, member.mode,
        digest, member.devmajor, member.devminor, member.linkname, member.
        linkpath, member.uname, member.gname, member.mtime))
    if close:
        conn.close()