def _check_section(cls, docstring, definition, context):
    capitalized_section = context.section_name.title()
    indentation = cls._get_docstring_indent(definition, docstring)
    if (context.section_name not in cls.SECTION_NAMES and 
        capitalized_section in cls.SECTION_NAMES):
        yield violations.D405(capitalized_section, context.section_name)
    if leading_space(context.line) > indentation:
        yield violations.D214(capitalized_section)
    suffix = context.line.strip().lstrip(context.section_name)
    if suffix:
        yield violations.D406(capitalized_section, context.line.strip())
    if not context.following_lines or not is_blank(context.following_lines[-1]
        ):
        if context.is_last_section:
            yield violations.D413(capitalized_section)
        else:
            yield violations.D410(capitalized_section)
    if not is_blank(context.previous_line):
        yield violations.D411(capitalized_section)
    for err in cls._check_section_underline(capitalized_section, context,
        indentation):
        yield err