def _get_files(sample):
    analysis = sample.get('analysis')
    if analysis.lower() in ['variant', 'snp calling', 'variant2', 'standard']:
        return _get_files_variantcall(sample)
    elif analysis.lower() in ['rna-seq', 'fastrna-seq']:
        return _get_files_rnaseq(sample)
    elif analysis.lower() in ['smallrna-seq']:
        return _get_files_srnaseq(sample)
    elif analysis.lower() in ['chip-seq']:
        return _get_files_chipseq(sample)
    elif analysis.lower() in ['scrna-seq']:
        return _get_files_scrnaseq(sample)
    else:
        return []