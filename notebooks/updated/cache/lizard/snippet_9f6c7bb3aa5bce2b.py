def docstring_with_summary(docstring, pairs, key_header, summary_type):
    return '\n'.join([docstring, 'Summary of {}:'.format(summary_type), ''] +
        summary_table(pairs, key_header) + [''])