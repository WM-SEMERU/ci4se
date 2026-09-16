def get_source(fileobj):
    if not isinstance(fileobj, dict):
        return fileobj
    else:
        try:
            with io.open(fileobj['filename'], encoding='utf-8', errors='ignore'
                ) as f:
                return f.read()
        finally:
            if fileobj.get('delete_after_use'):
                try:
                    os.remove(fileobj['filename'])
                except:
                    pass