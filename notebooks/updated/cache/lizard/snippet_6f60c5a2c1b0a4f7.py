def is_running(process):
    if os.name == 'nt':
        process_list = get_cmd_out(['tasklist', '/v'])
        return process in process_list
    else:
        process_list = get_cmd_out("ps axw | awk '{print $5}'")
        for i in process_list.split('\n'):
            if not i == 'COMMAND' or i.startswith('['):
                if i == process:
                    return True
                elif os.path.basename(i) == process:
                    return True
    return False