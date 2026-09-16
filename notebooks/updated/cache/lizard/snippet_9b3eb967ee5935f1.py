def minify(path):
    if 'http' in path:
        data = requests.get(path).content.decode('ascii', errors='ignore')
    else:
        with open(path, 'rb') as f:
            data = f.read().decode('ascii', errors='ignore')
    if '.min.' in path:
        return data
    try:
        return jsmin.jsmin(data)
    except BaseException:
        return data