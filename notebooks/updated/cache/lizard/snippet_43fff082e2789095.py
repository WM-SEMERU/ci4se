def generate_py_abilities(data):

    def print_action(func_id, name, func, ab_id, general_id):
        args = [func_id, '"%s"' % name, func, ab_id]
        if general_id:
            args.append(general_id)
        print('    Function.ability(%s),' % ', '.join(str(v) for v in args))
    func_ids = itertools.count(12)
    for ability in sorted(six.itervalues(data.abilities), key=lambda a:
        sort_key(data, a)):
        ab_id = ability.ability_id
        if (ab_id in skip_abilities or ab_id not in data.general_abilities and
            ab_id not in used_abilities):
            continue
        name = generate_name(ability).replace(' ', '_')
        if ability.target in (sc_data.AbilityData.Target.Value('None'),
            sc_data.AbilityData.PointOrNone):
            print_action(next(func_ids), name + '_quick', 'cmd_quick',
                ab_id, ability.remaps_to_ability_id)
        if ability.target != sc_data.AbilityData.Target.Value('None'):
            print_action(next(func_ids), name + '_screen', 'cmd_screen',
                ab_id, ability.remaps_to_ability_id)
            if ability.allow_minimap:
                print_action(next(func_ids), name + '_minimap',
                    'cmd_minimap', ab_id, ability.remaps_to_ability_id)
        if ability.allow_autocast:
            print_action(next(func_ids), name + '_autocast', 'autocast',
                ab_id, ability.remaps_to_ability_id)