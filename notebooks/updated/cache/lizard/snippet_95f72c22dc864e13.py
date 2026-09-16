def prepare_subprocess_cmd(subprocess_cmd):
    help_cmd = subprocess_cmd + ['--helpfull']
    help_output = subprocess.run(help_cmd, stdout=subprocess.PIPE).stdout
    help_output = help_output.decode('ascii')
    if 'python' in subprocess_cmd[0]:
        valid_flags = parse_helpfull_output(help_output)
    else:
        valid_flags = parse_helpfull_output(help_output, regex=FLAG_HELP_RE_CC)
    parsed_flags = flags.FlagValues().read_flags_from_files(subprocess_cmd[1:])
    filtered_flags = filter_flags(parsed_flags, valid_flags)
    return [subprocess_cmd[0]] + filtered_flags