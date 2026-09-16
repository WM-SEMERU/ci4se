def extract_variables(content):
    if isinstance(content, (list, set, tuple)):
        variables = set()
        for item in content:
            variables = variables | extract_variables(item)
        return variables
    elif isinstance(content, dict):
        variables = set()
        for key, value in content.items():
            variables = variables | extract_variables(value)
        return variables
    elif isinstance(content, LazyString):
        return set(regex_findall_variables(content.raw_string))
    return set()