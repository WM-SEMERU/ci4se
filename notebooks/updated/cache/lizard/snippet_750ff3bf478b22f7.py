def _run_cromwell(args):
    main_file, json_file, project_name = _get_main_and_json(args.directory)
    work_dir = utils.safe_makedir(os.path.join(os.getcwd(), 'cromwell_work'))
    final_dir = utils.safe_makedir(os.path.join(work_dir, 'final'))
    if args.no_container:
        _remove_bcbiovm_path()
    log_file = os.path.join(work_dir, '%s-cromwell.log' % project_name)
    metadata_file = os.path.join(work_dir, '%s-metadata.json' % project_name)
    option_file = os.path.join(work_dir, '%s-options.json' % project_name)
    cromwell_opts = {'final_workflow_outputs_dir': final_dir,
        'default_runtime_attributes': {'bootDiskSizeGb': 20}}
    with open(option_file, 'w') as out_handle:
        json.dump(cromwell_opts, out_handle)
    cmd = ['cromwell', '-Xms1g', '-Xmx%s' % _estimate_runner_memory(
        json_file), 'run', '--type', 'CWL', '-Dconfig.file=%s' % hpc.
        create_cromwell_config(args, work_dir, json_file)]
    cmd += hpc.args_to_cromwell_cl(args)
    cmd += ['--metadata-output', metadata_file, '--options', option_file,
        '--inputs', json_file, main_file]
    with utils.chdir(work_dir):
        _run_tool(cmd, not args.no_container, work_dir, log_file)
        if metadata_file and utils.file_exists(metadata_file):
            with open(metadata_file) as in_handle:
                metadata = json.load(in_handle)
            if metadata['status'] == 'Failed':
                _cromwell_debug(metadata)
                sys.exit(1)
            else:
                _cromwell_move_outputs(metadata, final_dir)