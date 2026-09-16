def format_explanation(explanation, indent='  ', indent_level=0):
    if not explanation:
        return ''
    line = '%s%s %2.4f' % (indent * indent_level, explanation['description'
        ], explanation['value'])
    if 'details' in explanation:
        details = '\n'.join([format_explanation(subtree, indent, 
            indent_level + 1) for subtree in explanation['details']])
        return line + '\n' + details
    return line