def _check_hetcaller(item):
    svs = _get_as_list(item, 'svcaller')
    hets = _get_as_list(item, 'hetcaller')
    if hets or any([(x in svs) for x in ['titancna', 'purecn']]):
        if not any([(x in svs) for x in ['cnvkit', 'gatk-cnv']]):
            raise ValueError(
                'Heterogeneity caller used but need CNV calls. Add `gatk4-cnv` or `cnvkit` to `svcaller` in sample: %s'
                 % item['description'])