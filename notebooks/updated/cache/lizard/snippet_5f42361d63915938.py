def guess_content_type(self, pathname):
    file_basename = os.path.basename(pathname)
    content_type = None
    if not content_type and self._filename_map.has_key(file_basename):
        content_type = self._filename_map[file_basename]
    if not content_type and '.' in file_basename:
        extension = '.' + file_basename.split('.')[-1]
        extension = extension_case_transform_func(extension)
        try:
            content_type = self._extension_map[extension]
        except KeyError:
            pass
    if not content_type:
        for regexp, _content_type in self._regexp_map.iteritems():
            if regexp.search(file_basename):
                content_type = _content_type
                break
    if os.path.exists(pathname):
        with open(pathname, 'rb') as f:
            content = f.read()
            if content.startswith('<?xml'):
                content_type = 'XML'
    return content_type