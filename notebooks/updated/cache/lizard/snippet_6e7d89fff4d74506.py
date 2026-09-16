def put_key(self, source, rel_path):
    k = self._get_boto_key(rel_path)
    try:
        k.set_contents_from_file(source)
    except AttributeError:
        if os.path.getsize(source) > 4.8 * 1024 * 1024 * 1024:
            k.set_contents_from_filename(source)
        else:
            k.set_contents_from_filename(source)