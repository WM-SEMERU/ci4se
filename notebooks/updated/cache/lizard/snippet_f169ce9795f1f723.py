def namespace_to_regex(namespace):
    db_name, coll_name = namespace.split('.', 1)
    db_regex = re.escape(db_name).replace('\\*', '([^.]*)')
    coll_regex = re.escape(coll_name).replace('\\*', '(.*)')
    return re.compile('\\A' + db_regex + '\\.' + coll_regex + '\\Z')