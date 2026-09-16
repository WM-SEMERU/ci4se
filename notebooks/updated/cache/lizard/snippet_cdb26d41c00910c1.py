def execute(self, env, args):
    task_name = args.task_name
    clone_task = args.clone_task
    if not env.task.create(task_name, clone_task):
        raise errors.FocusError('Could not create task "{0}"'.format(task_name)
            )
    if not args.skip_edit:
        task_config = env.task.get_config_path(task_name)
        if not _edit_task_config(env, task_config, confirm=True):
            raise errors.FocusError('Could not open task config: {0}'.
                format(task_config))