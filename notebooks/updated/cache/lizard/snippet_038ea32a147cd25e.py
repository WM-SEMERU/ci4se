def savepoint(cr):
    if hasattr(cr, 'savepoint'):
        with cr.savepoint():
            yield
    else:
        name = uuid.uuid1().hex
        cr.execute('SAVEPOINT "%s"' % name)
        try:
            yield
            cr.execute('RELEASE SAVEPOINT "%s"' % name)
        except:
            cr.execute('ROLLBACK TO SAVEPOINT "%s"' % name)