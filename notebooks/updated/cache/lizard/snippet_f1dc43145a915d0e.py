def actions(self):
    r = self.session.query(models.Action).all()
    return [x.type_name for x in r]