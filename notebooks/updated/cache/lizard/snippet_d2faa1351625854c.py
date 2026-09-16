def readme():
    path = os.path.realpath(os.path.join(os.path.dirname(__file__),
        'README.rst'))
    handle = None
    url_prefix = (
        'https://raw.githubusercontent.com/Robpol86/{name}/v{version}/'.
        format(name=NAME, version=VERSION))
    try:
        handle = codecs.open(path, encoding='utf-8')
        return handle.read(131072).replace('.. image:: docs',
            '.. image:: {0}docs'.format(url_prefix))
    except IOError:
        return ''
    finally:
        getattr(handle, 'close', lambda : None)()