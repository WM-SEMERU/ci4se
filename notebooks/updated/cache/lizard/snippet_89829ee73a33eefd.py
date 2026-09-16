def _get_variant_file(x, key, suffix='', sample=None, ignore_do_upload=False):
    out = []
    fname = utils.get_in(x, key)
    upload_key = list(key)
    upload_key[-1] = 'do_upload'
    do_upload = tz.get_in(tuple(upload_key), x, True)
    if fname and (ignore_do_upload or do_upload):
        if fname.endswith('.vcf.gz'):
            out.append({'path': fname, 'type': 'vcf.gz', 'ext': '%s%s' % (x
                ['variantcaller'], suffix), 'variantcaller': x[
                'variantcaller']})
            if utils.file_exists(fname + '.tbi'):
                out.append({'path': fname + '.tbi', 'type': 'vcf.gz.tbi',
                    'index': True, 'ext': '%s%s' % (x['variantcaller'],
                    suffix), 'variantcaller': x['variantcaller']})
        elif fname.endswith(('.vcf', '.bed', '.bedpe', '.bedgraph', '.cnr',
            '.cns', '.cnn', '.txt', '.tsv')):
            ftype = utils.splitext_plus(fname)[-1][1:]
            if ftype == 'txt':
                extended_ftype = fname.split('-')[-1]
                if '/' not in extended_ftype:
                    ftype = extended_ftype
            out.append({'path': fname, 'type': ftype, 'ext': '%s%s' % (x[
                'variantcaller'], suffix), 'variantcaller': x['variantcaller']}
                )
    if sample:
        out_sample = []
        for x in out:
            x['sample'] = sample
            out_sample.append(x)
        return out_sample
    else:
        return out