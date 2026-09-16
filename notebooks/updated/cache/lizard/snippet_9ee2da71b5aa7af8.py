def create_tags(user):
    values = {'id': utils.gen_uuid(), 'created_at': datetime.datetime.
        utcnow().isoformat()}
    values.update(schemas.tag.post(flask.request.json))
    with flask.g.db_conn.begin():
        where_clause = sql.and_(_TABLE.c.name == values['name'])
        query = sql.select([_TABLE.c.id]).where(where_clause)
        if flask.g.db_conn.execute(query).fetchone():
            raise dci_exc.DCIConflict('Tag already exists', values)
        query = _TABLE.insert().values(**values)
        flask.g.db_conn.execute(query)
        result = json.dumps({'tag': values})
        return flask.Response(result, 201, content_type='application/json')