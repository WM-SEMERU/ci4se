def create(context, name, component_types, active, product_id, data):
    if component_types:
        component_types = component_types.split(',')
    state = utils.active_string(active)
    result = topic.create(context, name=name, component_types=
        component_types, state=state, product_id=product_id, data=data)
    utils.format_output(result, context.format)