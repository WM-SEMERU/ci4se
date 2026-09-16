def cmd_quick(action, action_space, ability_id, queued):
    action_cmd = spatial(action, action_space).unit_command
    action_cmd.ability_id = ability_id
    action_cmd.queue_command = queued