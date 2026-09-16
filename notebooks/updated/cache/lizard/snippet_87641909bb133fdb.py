def do_action(character, action):
    stats = 'Energy=' + str(round(character['energy'], 0)) + ', '
    stats += 'Gold=' + str(round(character['gold'], 0)) + ', '
    ndx_action_skill = get_skill_by_name(action['name'], character)
    stats += 'Skill=' + str(round(character['skills'][ndx_action_skill][
        'level'], 1))
    my_char['energy'] -= action['cost_energy']
    my_char['skills'][ndx_action_skill]['level'] += action['exp_gain']
    reward_item = action['reward_item']
    inv = get_inventory_by_name(reward_item, my_char)
    if roll_dice(action['reward_chance']):
        my_char['inventory'][inv]['val'] += 1
        print(character['name'] + ' is ' + action['name'] + '. ' + stats +
            ' FOUND ' + reward_item)
    else:
        print(character['name'] + ' is ' + action['name'] + '. ' + stats)