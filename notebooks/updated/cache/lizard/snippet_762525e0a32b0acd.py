def gatk_haplotype_caller(job, bam, bai, ref, fai, ref_dict, annotations=
    None, emit_threshold=10.0, call_threshold=30.0, unsafe_mode=False,
    hc_output=None):
    job.fileStore.logToMaster('Running GATK HaplotypeCaller')
    inputs = {'genome.fa': ref, 'genome.fa.fai': fai, 'genome.dict':
        ref_dict, 'input.bam': bam, 'input.bam.bai': bai}
    work_dir = job.fileStore.getLocalTempDir()
    for name, file_store_id in inputs.iteritems():
        job.fileStore.readGlobalFile(file_store_id, os.path.join(work_dir,
            name))
    command = ['-T', 'HaplotypeCaller', '-nct', str(job.cores), '-R',
        'genome.fa', '-I', 'input.bam', '-o', 'output.g.vcf',
        '-stand_call_conf', str(call_threshold), '-stand_emit_conf', str(
        emit_threshold), '-variant_index_type', 'LINEAR',
        '-variant_index_parameter', '128000', '--genotyping_mode',
        'Discovery', '--emitRefConfidence', 'GVCF']
    if unsafe_mode:
        command = ['-U', 'ALLOW_SEQ_DICT_INCOMPATIBILITY'] + command
    if annotations:
        for annotation in annotations:
            command.extend(['-A', annotation])
    outputs = {'output.g.vcf': hc_output}
    docker_call(job=job, work_dir=work_dir, env={'JAVA_OPTS':
        '-Djava.io.tmpdir=/data/ -Xmx{}'.format(job.memory)}, parameters=
        command, tool=
        'quay.io/ucsc_cgl/gatk:3.5--dba6dae49156168a909c43330350c6161dc7ecc2',
        inputs=inputs.keys(), outputs=outputs, mock=True if outputs[
        'output.g.vcf'] else False)
    return job.fileStore.writeGlobalFile(os.path.join(work_dir, 'output.g.vcf')
        )