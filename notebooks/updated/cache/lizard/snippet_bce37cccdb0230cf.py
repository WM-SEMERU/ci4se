def autocast(action, action_space, ability_id):
    del action_space
    action.action_ui.toggle_autocast.ability_id = ability_id