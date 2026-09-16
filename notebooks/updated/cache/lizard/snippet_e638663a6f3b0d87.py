def tree_line_generator(el, max_lines=None):

    def _trim_spaces(text):
        return MULTIPLE_WHITESPACE_RE.sub(' ', text).strip()
    counter = 1
    if max_lines != None and counter > max_lines:
        return
    line = ''
    start_ref = None
    start_indentation_level = None
    for token in tree_token_generator(el):
        if token is None:
            continue
        elif isinstance(token, tuple):
            el, state, indentation_level = token
            tag_name = el.tag.lower()
            line_break = tag_name == 'br' and state == BEGIN
            is_block = tag_name not in INLINE_TAGS
            is_forward = is_block and state == BEGIN and el.attrib.get('style'
                ) in FORWARD_STYLES
            if is_block or line_break:
                line = _trim_spaces(line)
                if line or line_break or is_forward:
                    end_ref = el, state
                    yield start_ref, end_ref, start_indentation_level, line
                    counter += 1
                    if max_lines != None and counter > max_lines:
                        return
                    line = ''
                    if is_forward:
                        yield end_ref, end_ref, start_indentation_level, FORWARD_LINE
                        counter += 1
                        if max_lines != None and counter > max_lines:
                            return
                if not line:
                    start_ref = el, state
                    start_indentation_level = indentation_level
        elif isinstance(token, string_class):
            line += token
        else:
            raise RuntimeError('invalid token: {}'.format(token))
    line = _trim_spaces(line)
    if line:
        yield line