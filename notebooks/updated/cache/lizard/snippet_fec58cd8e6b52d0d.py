def StaticServe(base_path='/views/static/'):

    def get_file(path=RAW_INVOCATION_ARGS):
        fullpath = get_config('project_path') + os.path.join(base_path, path)
        try:
            mime, encoding = mimetypes.guess_type(fullpath)
            return open(fullpath, 'rb'), mime or 'application/octet-stream'
        except IOError:
            raise DataNotFound('File does not exist')


    class StaticServe(Program):
        controllers = ['http-get']
        model = [get_file]
        view = FileView()
    return StaticServe()