def fix_line_range(source_code, start, end, options):
    start = max(start, 1)
    options.line_range = [start, end]
    from autopep8 import fix_code
    fixed = fix_code(source_code, options)
    try:
        if options.docformatter:
            from docformatter import format_code
            fixed = format_code(fixed, summary_wrap_length=options.
                max_line_length - 1, description_wrap_length=options.
                max_line_length - 2 * options.indent_size,
                pre_summary_newline=options.pre_summary_newline,
                post_description_blank=options.post_description_blank,
                force_wrap=options.force_wrap, line_range=[start, end])
    except AttributeError:
        pass
    return fixed