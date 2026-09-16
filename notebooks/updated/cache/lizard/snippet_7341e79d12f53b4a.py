def save(self, target, ensure_ascii=True):
    mode = 'w'
    encoding = 'utf-8'
    if six.PY2:
        mode = 'wb'
        encoding = None
    helpers.ensure_dir(target)
    with io.open(target, mode=mode, encoding=encoding) as file:
        json.dump(self.__current_descriptor, file, indent=4, ensure_ascii=
            ensure_ascii)