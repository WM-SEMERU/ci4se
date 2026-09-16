def add_path_part(url, regex=PATH_PART):
    formatter = string.Formatter()
    url_var_template = '(?P<{var_name}>{regex})'
    for part in formatter.parse(url):
        string_part, var_name, _, _ = part
        if string_part:
            yield string_part
        if var_name:
            yield url_var_template.format(var_name=var_name, regex=regex)