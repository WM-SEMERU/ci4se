def view_task_durations(token, dstore):
    task = token.split(':')[1]
    array = dstore['task_info/' + task]['duration']
    return '\n'.join(map(str, array))