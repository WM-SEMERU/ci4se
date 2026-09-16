def _run_concat_variant_files_gatk4(input_file_list, out_file, config):
    if not utils.file_exists(out_file):
        with file_transaction(config, out_file) as tx_out_file:
            params = ['-T', 'GatherVcfs', '-I', input_file_list, '-O',
                tx_out_file]
            config = utils.deepish_copy(config)
            if 'gatk4' in dd.get_tools_off({'config': config}):
                config['algorithm']['tools_off'].remove('gatk4')
            resources = config_utils.get_resources('gatk', config)
            opts = [str(x) for x in resources.get('options', [])]
            if '--verbosity' in opts:
                params += ['--VERBOSITY:%s' % opts[opts.index('--verbosity'
                    ) + 1]]
            broad_runner = broad.runner_from_config(config)
            broad_runner.run_gatk(params)
    return out_file