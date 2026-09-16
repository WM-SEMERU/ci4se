def _get_header_correctly_cased(header_name):
    header_name = header_name.capitalize()
    matches = re.findall(_REGEX_FOR_LOWERCASE_HEADERS, header_name)
    for match in matches:
        header_name = re.sub(match, match.upper(), header_name)
    return header_name