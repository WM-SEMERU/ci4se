def regroup_commands(commands):
    grouped = []
    pending = []

    def group_pending():
        if not pending:
            return
        new_command = grouped_command(pending)
        result = []
        while pending:
            result.append(pending.pop(0))
        grouped.append((new_command, result))
    for command, next_command in peek(commands):
        if can_group_commands(command, next_command):
            if pending and not can_group_commands(pending[0], command):
                group_pending()
            pending.append(command)
        else:
            if pending and can_group_commands(pending[0], command):
                pending.append(command)
            else:
                grouped.append((command.clone(), [command]))
            group_pending()
    group_pending()
    return grouped