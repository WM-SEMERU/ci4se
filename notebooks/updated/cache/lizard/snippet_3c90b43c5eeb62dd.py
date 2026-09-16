def _check_exists(database: Database, table: LdapObjectClass, key: str,
    value: str):
    try:
        get_one(table, Q(**{key: value}), database=database)
        return True
    except ObjectDoesNotExist:
        return False