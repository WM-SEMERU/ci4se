def _pyside2():
    import PySide2 as module
    _setup(module, ['QtUiTools'])
    Qt.__binding_version__ = module.__version__
    try:
        try:
            import shiboken2
        except ImportError:
            from PySide2 import shiboken2
        Qt.QtCompat.wrapInstance = lambda ptr, base=None: _wrapinstance(
            shiboken2.wrapInstance, ptr, base)
        Qt.QtCompat.getCppPointer = lambda object: shiboken2.getCppPointer(
            object)[0]
    except ImportError:
        pass
    if hasattr(Qt, '_QtUiTools'):
        Qt.QtCompat.loadUi = _loadUi
    if hasattr(Qt, '_QtCore'):
        Qt.__qt_version__ = Qt._QtCore.qVersion()
        Qt.QtCompat.qInstallMessageHandler = _qInstallMessageHandler
        Qt.QtCompat.translate = Qt._QtCore.QCoreApplication.translate
    if hasattr(Qt, '_QtWidgets'):
        Qt.QtCompat.setSectionResizeMode = (Qt._QtWidgets.QHeaderView.
            setSectionResizeMode)
    _reassign_misplaced_members('PySide2')
    _build_compatibility_members('PySide2')