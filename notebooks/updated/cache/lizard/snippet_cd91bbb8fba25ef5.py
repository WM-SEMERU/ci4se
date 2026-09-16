def create_handler(Model, name=None, **kwds):

    async def action_handler(service, action_type, payload, props, notify=
        True, **kwds):
        if action_type == get_crud_action('create', name or Model):
            try:
                message_props = {}
                if 'correlation_id' in props:
                    message_props['correlation_id'] = props['correlation_id']
                for requirement in Model.required_fields():
                    field_name = requirement.name
                    if not field_name in payload and field_name != 'id':
                        raise ValueError(
                            'Required field not found in payload: %s' %
                            field_name)
                new_model = Model(**payload)
                new_model.save()
                if notify:
                    await service.event_broker.send(payload=ModelSerializer
                        ().serialize(new_model), action_type=
                        change_action_status(action_type, success_status()),
                        **message_props)
            except Exception as err:
                if notify:
                    await service.event_broker.send(payload=str(err),
                        action_type=change_action_status(action_type,
                        error_status()), **message_props)
                else:
                    raise err
    return action_handler