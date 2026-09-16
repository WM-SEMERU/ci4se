def process_docstring(app, what, name, obj, options, lines):
    lines.extend(_format_contracts(what=what, obj=obj))