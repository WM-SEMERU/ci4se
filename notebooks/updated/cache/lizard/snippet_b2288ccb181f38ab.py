def parse_ctcp(query):
    query = query.strip(CTCP_DELIMITER)
    query = query.replace(CTCP_ESCAPE_CHAR + '0', '\x00')
    query = query.replace(CTCP_ESCAPE_CHAR + 'n', '\n')
    query = query.replace(CTCP_ESCAPE_CHAR + 'r', '\r')
    query = query.replace(CTCP_ESCAPE_CHAR + CTCP_ESCAPE_CHAR, CTCP_ESCAPE_CHAR
        )
    if ' ' in query:
        return query.split(' ', 1)
    return query, None