def step_use_curdir_as_working_directory(context):
    context.workdir = os.path.abspath('.')
    command_util.ensure_workdir_exists(context)