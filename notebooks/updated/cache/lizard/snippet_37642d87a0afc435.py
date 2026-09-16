def get_subdomains_owned_by_address(self, owner, cur=None):
    get_cmd = (
        'SELECT fully_qualified_subdomain, MAX(sequence) FROM {} WHERE owner = ? AND accepted=1 GROUP BY fully_qualified_subdomain'
        .format(self.subdomain_table))
    cursor = None
    if cur is None:
        cursor = self.conn.cursor()
    else:
        cursor = cur
    db_query_execute(cursor, get_cmd, (owner,))
    try:
        return [x['fully_qualified_subdomain'] for x in cursor.fetchall()]
    except Exception as e:
        if BLOCKSTACK_DEBUG:
            log.exception(e)
        return []