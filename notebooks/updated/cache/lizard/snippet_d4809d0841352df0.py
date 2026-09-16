def ReadGRRUser(self, username, cursor=None):
    cursor.execute(
        'SELECT username, password, ui_mode, canary_mode, user_type FROM grr_users WHERE username_hash = %s'
        , [mysql_utils.Hash(username)])
    row = cursor.fetchone()
    if row is None:
        raise db.UnknownGRRUserError(username)
    return self._RowToGRRUser(row)