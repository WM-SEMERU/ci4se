def zinnia_loop_template(context, default_template):
    matching, context_object = get_context_first_matching_object(context, [
        'category', 'tag', 'author', 'pattern', 'year', 'month', 'week', 'day']
        )
    context_positions = get_context_loop_positions(context)
    templates = loop_template_list(context_positions, context_object,
        matching, default_template, ENTRY_LOOP_TEMPLATES)
    return select_template(templates)