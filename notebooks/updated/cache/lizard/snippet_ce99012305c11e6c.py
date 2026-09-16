def comittoapi(api):
    global USED_API
    assert USED_API is None, 'committoapi called again!'
    check = ['PyQt4', 'PyQt5', 'PySide', 'PySide2']
    assert api in [QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2]
    for name in check:
        if name.lower() != api and name in sys.modules:
            raise RuntimeError('{} was already imported. Cannot commit to {}!'
                .format(name, api))
    else:
        api = _intern(api)
        USED_API = api
        AnyQt.__SELECTED_API = api
        AnyQt.USED_API = api