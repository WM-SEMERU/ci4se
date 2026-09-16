def _split_markdown(text_url, tld_pos):
    left_bracket_pos = text_url.find('[')
    if left_bracket_pos > tld_pos - 3:
        return text_url
    right_bracket_pos = text_url.find(')')
    if right_bracket_pos < tld_pos:
        return text_url
    middle_pos = text_url.rfind('](')
    if middle_pos > tld_pos:
        return text_url[left_bracket_pos + 1:middle_pos]
    return text_url