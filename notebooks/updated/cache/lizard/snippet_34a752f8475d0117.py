def deblur_system_call(params, input_fp):
    logger = logging.getLogger(__name__)
    logger.debug('[%s] deblur system call params %s, input_fp %s' % (mp.
        current_process().name, params, input_fp))
    script_name = 'deblur'
    script_subprogram = 'workflow'
    command = [script_name, script_subprogram, '--seqs-fp', input_fp,
        '--is-worker-thread', '--keep-tmp-files']
    command.extend(params)
    logger.debug('[%s] running command %s' % (mp.current_process().name,
        command))
    return _system_call(command)