def first_paragraph_indent(indent_texts):
    opening_indent = determine_opening_indent(indent_texts)
    result = []
    input = iter(indent_texts)
    for indent, text in input:
        if indent == 0:
            result.append((opening_indent, text))
        else:
            result.append((indent, text))
            break
    for indent, text in input:
        result.append((indent, text))
    return result