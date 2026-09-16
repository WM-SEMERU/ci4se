def cli_info(data, title='Info'):
    wrapper = textwrap.TextWrapper()
    wrapper.initial_indent = ' ' * 4
    wrapper.subsequent_indent = wrapper.initial_indent
    return '{title}:\n\n{text}'.format(title=title, text=wrapper.fill(data))