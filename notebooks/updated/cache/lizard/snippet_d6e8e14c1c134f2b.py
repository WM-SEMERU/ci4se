def escape(text, newline=False):
    if isinstance(text, basestring):
        if '&' in text:
            text = text.replace('&', '&amp;')
        if '>' in text:
            text = text.replace('>', '&gt;')
        if '<' in text:
            text = text.replace('<', '&lt;')
        if '"' in text:
            text = text.replace('"', '&quot;')
        if "'" in text:
            text = text.replace("'", '&quot;')
        if newline:
            if '\n' in text:
                text = text.replace('\n', '<br>')
    return text