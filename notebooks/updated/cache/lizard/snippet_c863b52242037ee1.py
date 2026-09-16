def run_terraform_init(tf_bin, module_path, backend_options, env_name,
    env_region, env_vars):
    init_cmd = [tf_bin, 'init']
    cmd_opts = {'env_vars': env_vars, 'exit_on_error': False}
    if backend_options.get('config'):
        LOGGER.info('Using provided backend values "%s"', str(
            backend_options.get('config')))
        cmd_opts['cmd_list'] = init_cmd + get_backend_init_list(backend_options
            .get('config'))
    elif os.path.isfile(os.path.join(module_path, backend_options.get(
        'filename'))):
        LOGGER.info('Using backend config file %s', backend_options.get(
            'filename'))
        cmd_opts['cmd_list'] = init_cmd + ['-backend-config=%s' %
            backend_options.get('filename')]
    else:
        LOGGER.info(
            'No backend tfvars file found -- looking for one of "%s" (proceeding with bare \'terraform init\')'
            , ', '.join(gen_backend_tfvars_files(env_name, env_region)))
        cmd_opts['cmd_list'] = init_cmd
    try:
        run_module_command(**cmd_opts)
    except subprocess.CalledProcessError as shelloutexc:
        if os.path.isdir(os.path.join(module_path, '.terraform')):
            with open(os.path.join(module_path, '.terraform',
                FAILED_INIT_FILENAME), 'w') as stream:
                stream.write('1')
        sys.exit(shelloutexc.returncode)