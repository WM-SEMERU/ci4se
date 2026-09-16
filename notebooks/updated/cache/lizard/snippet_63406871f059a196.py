def _get_project_name(args):
    name = args.get(0)
    puts('')
    while not name:
        name = raw_input(
            "What is the project's short directory name? (e.g. my_project) ")
    return name