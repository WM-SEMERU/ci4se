def edit_history(self):
    ret = self._db.session.query(Config).filter(Config.type == 'buildstate'
        ).filter(Config.group == 'access').filter(Config.key == 'last'
        ).order_by(Config.modified.desc()).all()
    return ret