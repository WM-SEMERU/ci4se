def switch_delete_record_for_userid(self, userid):
    with get_network_conn() as conn:
        conn.execute('DELETE FROM switch WHERE userid=?', (userid,))
        LOG.debug('Switch record for user %s is removed from switch table' %
            userid)