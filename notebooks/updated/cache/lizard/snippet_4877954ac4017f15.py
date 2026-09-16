def get(self, filepath):
    contents = self.get_argument('contents', False)
    if contents == 'true':
        contents = True
    else:
        contents = False
    dir_sizes = self.get_argument('dir_sizes', False)
    if dir_sizes == 'true':
        dir_sizes = True
    else:
        dir_sizes = False
    try:
        res = self.fs.get_directory_details(filepath, contents=contents,
            dir_sizes=dir_sizes)
        res = res.to_dict()
        self.write(res)
    except OSError:
        raise tornado.web.HTTPError(404)