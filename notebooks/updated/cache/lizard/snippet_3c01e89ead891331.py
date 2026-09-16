def _execute(self, connection, query, fetch=True):
    with connection.cursor() as cursor:
        cursor.execute(query)
        if fetch:
            return cursor.fetchall()
        else:
            cursor.execute('COMMIT;')