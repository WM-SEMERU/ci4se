def pyc2py(filename):
    if re.match('.*py[co]$', filename):
        if PYTHON3:
            return re.sub('(.*)__pycache__/(.+)\\.cpython-%s.py[co]$' %
                PYVER, '\\1\\2.py', filename)
        else:
            return filename[:-1]
    return filename