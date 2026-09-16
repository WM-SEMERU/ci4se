def _get_snpeff_cmd(cmd_name, datadir, data, out_file):
    resources = config_utils.get_resources('snpeff', data['config'])
    jvm_opts = resources.get('jvm_opts', ['-Xms750m', '-Xmx3g'])
    jvm_opts = config_utils.adjust_opts(jvm_opts, {'algorithm': {
        'memory_adjust': {'direction': 'increase', 'maximum': '30000M',
        'magnitude': max(2, dd.get_cores(data))}}})
    memory = ' '.join(jvm_opts)
    snpeff = config_utils.get_program('snpEff', data['config'])
    java_args = '-Djava.io.tmpdir=%s' % utils.safe_makedir(os.path.join(os.
        path.dirname(out_file), 'tmp'))
    export = ('unset JAVA_HOME && export PATH=%s:"$PATH" && ' % utils.
        get_java_binpath())
    cmd = (
        '{export} {snpeff} {memory} {java_args} {cmd_name} -dataDir {datadir}')
    return cmd.format(**locals())