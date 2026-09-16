def addToDB(abbr=None, dbname=manualDBname):
    dbLoc = os.path.normpath(os.path.dirname(__file__))
    with dbm.dumb.open(dbLoc + '/' + dbname) as db:
        if isinstance(abbr, str):
            db[abbr] = abbr
        elif isinstance(abbr, dict):
            try:
                db.update(abbr)
            except TypeError:
                raise TypeError('The keys and values of abbr must be strings.')
        elif abbr is None:
            pass
        else:
            raise TypeError('abbr must be a str or dict.')