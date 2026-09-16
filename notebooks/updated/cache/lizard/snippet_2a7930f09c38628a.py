def delete_tag_for_component(user, c_id, tag_id):
    query = _TABLE_TAGS.delete().where(_TABLE_TAGS.c.tag_id == tag_id and 
        _TABLE_TAGS.c.component_id == c_id)
    try:
        flask.g.db_conn.execute(query)
    except sa_exc.IntegrityError:
        raise dci_exc.DCICreationConflict(_TABLE_TAGS.c.tag_id, 'tag_id')
    return flask.Response(None, 204, content_type='application/json')