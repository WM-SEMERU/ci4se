def get_descriptions(config, exam_lex, lexer):
    if config.BOOLEAN_STATES[config.config.get('Layout', 'command_description')
        ]:
        if config.BOOLEAN_STATES[config.config.get('Layout',
            'param_description')]:
            return VSplit([get_descript(exam_lex), get_vline(), get_param(
                lexer)])
        return get_descript(exam_lex)
    if config.BOOLEAN_STATES[config.config.get('Layout', 'param_description')]:
        return get_param(lexer)
    return get_empty()