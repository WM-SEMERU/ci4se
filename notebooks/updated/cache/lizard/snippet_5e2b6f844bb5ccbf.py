def get_response(self):
    res = ARBlockRes()
    for field in ['ARType', 'ARUUID', 'SessionKey']:
        res.setfieldval(field, self.getfieldval(field))
    return res