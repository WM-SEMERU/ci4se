def render_template(cmd_derived_from_alias, pos_args_table):
    try:
        cmd_derived_from_alias = normalize_placeholders(cmd_derived_from_alias,
            inject_quotes=True)
        template = jinja.Template(cmd_derived_from_alias)
        rendered = shlex.split(template.render(pos_args_table))
        if '' in rendered:
            check_runtime_errors(cmd_derived_from_alias, pos_args_table)
        return rendered
    except Exception as exception:
        if isinstance(exception, CLIError):
            raise
        split_exception_message = str(exception).split()
        error_index = split_exception_message[-1]
        if error_index.isdigit():
            split_exception_message.insert(-1, 'index')
            error_msg = RENDER_TEMPLATE_ERROR.format(' '.join(
                split_exception_message), cmd_derived_from_alias)
            error_msg += '\n{}^'.format(' ' * (len(error_msg) - len(
                cmd_derived_from_alias) + int(error_index) - 1))
        else:
            exception_str = str(exception).replace('"{{', '}}').replace('}}"',
                '}}')
            error_msg = RENDER_TEMPLATE_ERROR.format(cmd_derived_from_alias,
                exception_str)
        raise CLIError(error_msg)