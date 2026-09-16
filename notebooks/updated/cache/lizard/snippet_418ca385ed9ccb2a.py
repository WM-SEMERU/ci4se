def _exec_command_to_file(adb_cmd, dest_file_handler):
    t = tempfile.TemporaryFile()
    final_adb_cmd = []
    for e in adb_cmd:
        if e != '':
            final_adb_cmd.append(e)
    print('\n*** Executing ' + ' '.join(adb_cmd) + ' ' + 'command')
    try:
        output = call(final_adb_cmd, stdout=dest_file_handler, stderr=t)
    except CalledProcessError as e:
        t.seek(0)
        result = e.returncode, t.read()
    else:
        result = output
        dest_file_handler.close()
    return result