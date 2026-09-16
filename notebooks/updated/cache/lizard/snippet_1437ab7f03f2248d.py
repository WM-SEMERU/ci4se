def add_unit_to_channel(current):
    read_only = current.input['read_only']
    newly_added, existing = [], []
    for member_key in UnitModel.get_user_keys(current, current.input[
        'unit_key']):
        sb, new = Subscriber(current).objects.get_or_create(user_id=
            member_key, read_only=read_only, channel_id=current.input[
            'channel_key'])
        if new:
            newly_added.append(member_key)
        else:
            existing.append(member_key)
    current.output = {'existing': existing, 'newly_added': newly_added,
        'status': 'OK', 'code': 201}