def scan_resource(self, pkg, path):
    r
    for fname in resource_listdir(pkg, path):
        if fname.endswith(TABLE_EXT):
            table_path = posixpath.join(path, fname)
            with contextlib.closing(resource_stream(pkg, table_path)
                ) as stream:
                self.add_colortable(stream, posixpath.splitext(posixpath.
                    basename(fname))[0])