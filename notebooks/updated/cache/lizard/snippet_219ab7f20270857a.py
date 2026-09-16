def delete_user(self, user):
    assert self.user == 'catroot' or self.user == 'postgres'
    assert not user == 'public'
    con = self.connection or self._connect()
    cur = con.cursor()
    cur.execute('DROP SCHEMA {user} CASCADE;'.format(user=user))
    cur.execute('REVOKE USAGE ON SCHEMA public FROM {user};'.format(user=user))
    cur.execute('REVOKE SELECT ON ALL TABLES IN SCHEMA public FROM {user};'
        .format(user=user))
    cur.execute('DROP ROLE {user};'.format(user=user))
    self.stdout.write('REMOVED USER {user}\n'.format(user=user))
    if self.connection is None:
        con.commit()
        con.close()
    return self