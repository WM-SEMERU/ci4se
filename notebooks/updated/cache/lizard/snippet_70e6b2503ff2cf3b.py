def compile_resource(resource):
    return re.compile('^' + trim_resource(re.sub(':(\\w+)',
        '(?P<\\1>[\\w-]+?)', resource)) + '(\\?(?P<querystring>.*))?$')