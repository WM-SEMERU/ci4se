def install_user_command_legacy(command, **substitutions):
    path = flo('~/bin/{command}')
    install_file_legacy(path, **substitutions)
    run(flo('chmod 755 {path}'))