def _obj_cursor_to_dictionary(self, cursor):
    if not cursor:
        return cursor
    cursor = json.loads(json.dumps(cursor, cls=BSONEncoder))
    if cursor.get('_id'):
        cursor['id'] = cursor.get('_id')
        del cursor['_id']
    return cursor