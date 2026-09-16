def escape_email_quoted_text(text, indent_txt='>>', linebreak_txt='\n'):
    washer = HTMLWasher()
    lines = text.split(linebreak_txt)
    output = ''
    for line in lines:
        line = line.strip()
        nb_indent = 0
        while True:
            if line.startswith(indent_txt):
                nb_indent += 1
                line = line[len(indent_txt):]
            else:
                break
        output += nb_indent * indent_txt + washer.wash(line,
            render_unallowed_tags=True) + linebreak_txt
        nb_indent = 0
    return output[:-1]