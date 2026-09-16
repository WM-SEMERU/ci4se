def _check_variantcaller(item):
    allowed = set(list(genotype.get_variantcallers().keys()) + [None, False])
    vcs = item['algorithm'].get('variantcaller')
    if not isinstance(vcs, dict):
        vcs = {'variantcaller': vcs}
    for vc_set in vcs.values():
        if not isinstance(vc_set, (tuple, list)):
            vc_set = [vc_set]
        problem = [x for x in vc_set if x not in allowed]
        if len(problem) > 0:
            raise ValueError(
                """Unexpected algorithm 'variantcaller' parameter: %s
Supported options: %s
"""
                 % (problem, sorted(list(allowed))))
    if 'germline' in vcs or 'somatic' in vcs:
        paired = vcfutils.get_paired_phenotype(item)
        if not paired:
            raise ValueError(
                "%s: somatic/germline calling in 'variantcaller' but tumor/normal metadata phenotype not specified"
                 % dd.get_sample_name(item))