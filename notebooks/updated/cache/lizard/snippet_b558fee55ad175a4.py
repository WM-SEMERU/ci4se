def quantitate_expression_parallel(samples, run_parallel):
    data = samples[0][0]
    samples = run_parallel('generate_transcript_counts', samples)
    if 'cufflinks' in dd.get_expression_caller(data):
        samples = run_parallel('run_cufflinks', samples)
    if 'stringtie' in dd.get_expression_caller(data):
        samples = run_parallel('run_stringtie_expression', samples)
    if 'kallisto' in dd.get_expression_caller(data) or dd.get_fusion_mode(data
        ) or 'pizzly' in dd.get_fusion_caller(data, []):
        samples = run_parallel('run_kallisto_index', [samples])
        samples = run_parallel('run_kallisto_rnaseq', samples)
    if 'sailfish' in dd.get_expression_caller(data):
        samples = run_parallel('run_sailfish_index', [samples])
        samples = run_parallel('run_sailfish', samples)
    samples = run_parallel('run_salmon_index', [samples])
    samples = run_parallel('run_salmon_reads', samples)
    samples = run_parallel('detect_fusions', samples)
    return samples