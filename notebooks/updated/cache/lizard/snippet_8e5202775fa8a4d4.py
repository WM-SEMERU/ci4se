def compose(cls, sub_commands, macros=None, cluster_label=None, notify=
    False, name=None, tags=None):
    if macros is not None:
        macros = json.loads(macros)
    return {'sub_commands': sub_commands, 'command_type':
        'CompositeCommand', 'macros': macros, 'label': cluster_label,
        'tags': tags, 'can_notify': notify, 'name': name}