def handle_exec(args):
    session_file = get_db_name(args.get('<session-file>'))
    cosmic_ray.commands.execute(session_file)
    return ExitCode.OK