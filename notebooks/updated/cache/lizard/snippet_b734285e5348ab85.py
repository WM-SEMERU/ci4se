def _run_command_inside_folder(command, folder):
    logger.debug('command: %s', command)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, cwd
        =folder)
    stream_data = process.communicate()[0]
    logger.debug('%s stdout: %s (RC %s)', command, stream_data, process.
        returncode)
    return process.returncode, stream_data