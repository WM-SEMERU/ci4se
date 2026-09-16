def execute_transactions(conn, statements: Iterable):
    with conn.cursor() as cursor:
        for statement in statements:
            try:
                cursor.execute(statement)
                conn.commit()
            except psycopg2.ProgrammingError:
                conn.rollback()