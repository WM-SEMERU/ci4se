def format_doc_text(text):
    return '\n'.join(textwrap.fill(line, width=99, initial_indent='    ',
        subsequent_indent='    ') for line in inspect.cleandoc(text).
        splitlines())