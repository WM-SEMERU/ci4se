def wrapinstance(ptr, base=None):
    if ptr is None:
        return None
    ptr = long(ptr)
    from wishlib.qt import active, QtCore, QtGui
    if active == 'PySide':
        import shiboken
        if base is None:
            qObj = shiboken.wrapInstance(ptr, QtCore.QObject)
            metaObj = qObj.metaObject()
            cls = metaObj.className()
            superCls = metaObj.superClass().className()
            if hasattr(QtGui, cls):
                base = getattr(QtGui, cls)
            elif hasattr(QtGui, superCls):
                base = getattr(QtGui, superCls)
            else:
                base = QtGui.QWidget
        return shiboken.wrapInstance(ptr, base)
    elif active == 'PyQt4':
        import sip
        return sip.wrapinstance(ptr, QtGui.QWidget)
    return None