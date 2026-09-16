def resource(string: str):
    try:
        prefix, resulting_type = Naming.pop_prefix(string)
        prefix += Naming.RESOURCE_PREFIX
    except IndexError:
        prefix = ''
        resulting_type = string
    resulting_type = dasherize(underscore(resulting_type))
    return prefix + (pluralize(resulting_type) if Naming._pluralize(
        resulting_type) else resulting_type)