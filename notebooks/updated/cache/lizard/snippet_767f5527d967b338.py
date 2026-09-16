def create_load():
    load = upkey('load').setResultsName('action')
    return load + Group(filename).setResultsName('load_file') + upkey('into'
        ) + table + Optional(throttle)