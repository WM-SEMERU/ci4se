def filled_out_template_str(template, **substitutions):
    template = template.replace('{', '{{')
    template = template.replace('}', '}}')
    template = template.replace('{{{{', '{')
    template = template.replace('}}}}', '}')
    template = template.format(**substitutions)
    template = template.replace('{{', '{')
    template = template.replace('}}', '}')
    template = template.replace('[[[', '{{')
    template = template.replace(']]]', '}}')
    return template