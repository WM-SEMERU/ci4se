def delete_tag_by_id(user, tag_id):
    query = _TABLE.delete().where(_TABLE.c.id == tag_id)
    result = flask.g.db_conn.execute(query)
    if not result.rowcount:
        raise dci_exc.DCIConflict('Tag deletion conflict', tag_id)
    return flask.Response(None, 204, content_type='application/json')