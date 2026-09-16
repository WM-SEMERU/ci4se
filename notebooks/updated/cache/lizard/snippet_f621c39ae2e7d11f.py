def align(fastq_file, pair_file, ref_file, names, align_dir, data,
    extra_args=None):
    config = data['config']
    rg_name = names.get('rg', None) if names else None
    out_file = os.path.join(align_dir, '%s-align.bam' % names['lane'])
    if not file_exists(out_file):
        with file_transaction(data, out_file) as tx_out_file:
            built_fastq = _convert_fastq(fastq_file, pair_file, rg_name,
                out_file, config)
            cl = [config_utils.get_program('mosaik', config, default=
                'MosaikAligner')]
            cl += _mosaik_args_from_config(config)
            cl += extra_args if extra_args is not None else []
            cl += ['-ia', ref_file, '-in', built_fastq, '-out', os.path.
                splitext(tx_out_file)[0]]
            jump_base = os.path.splitext(ref_file)[0]
            key_file = '{0}_keys.jmp'.format(jump_base)
            if file_exists(key_file):
                cl += ['-j', jump_base]
                jump_size_gb = os.path.getsize(key_file) / 1073741824.0
                if jump_size_gb < 1.0:
                    cl += ['-hs', '13']
            cl += _get_mosaik_nn_args(out_file)
            env_set = 'export MOSAIK_TMP={0}'.format(os.path.dirname(
                tx_out_file))
            subprocess.check_call(env_set + ' && ' + ' '.join([str(x) for x in
                cl]), shell=True)
            os.remove(built_fastq)
    return out_file