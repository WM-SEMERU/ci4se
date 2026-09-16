def tool_specific_param_generator(job, config_file):
    work_dir = job.fileStore.getLocalTempDir()
    group_params = defaultdict()
    group_name = None
    for line in config_file:
        line = line.strip()
        if line.startswith('##') or len(line) == 0:
            continue
        if line.startswith('#'):
            if group_name is None:
                group_name = line.lstrip('#').strip()
                continue
            else:
                yield group_name, group_params
                group_params = defaultdict(int)
                group_name = line.lstrip('#').strip()
                continue
        else:
            line = line.strip().split()
            if len(line) != 2:
                raise ParameterError(
                    'Found a problem in the config file while attempting to ' +
                    'parse %s in group %s' % (line[0], group_name) +
                    '.  Every ' + 'parameter takes ONLY one argument.')
            if [x for x in ['file', 'vcf', 'tar', 'fasta', 'fai', 'idx',
                'dict'] if x in line[0]]:
                group_params[line[0]] = job.addChildJobFn(get_pipeline_inputs,
                    line[0], line[1]).rv()
            else:
                group_params[line[0]] = line[1]
    yield group_name, group_params