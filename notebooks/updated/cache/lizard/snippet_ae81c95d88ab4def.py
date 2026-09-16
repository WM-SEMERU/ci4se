def extract_file_config(content):
    prop_pat = re.compile(
        '^\\s*#\\s*sphinx_gallery_([A-Za-z0-9_]+)\\s*=\\s*(.+)\\s*$', re.
        MULTILINE)
    file_conf = {}
    for match in re.finditer(prop_pat, content):
        name = match.group(1)
        value = match.group(2)
        try:
            value = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            logger.warning(
                'Sphinx-gallery option %s was passed invalid value %s',
                name, value)
        else:
            file_conf[name] = value
    return file_conf