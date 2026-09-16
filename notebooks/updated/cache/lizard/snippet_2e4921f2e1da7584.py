def _indexes_to_secondary_files(gresources, genome_build):
    out = {}
    for refname, val in gresources.items():
        if isinstance(val, dict) and 'indexes' in val:
            if len(val.keys()) == 1:
                indexes = sorted(val['indexes'])
                if len(indexes) == 0:
                    if refname not in alignment.allow_noindices():
                        raise ValueError('Did not find indexes for %s: %s' %
                            (refname, val))
                elif len(indexes) == 1:
                    val = {'indexes': indexes[0]}
                else:
                    val = {'indexes': {'base': indexes[0], 'indexes':
                        indexes[1:]}}
            elif 'base' in val and os.path.isdir(val['base']) and len(val[
                'indexes']) > 0:
                indexes = val['indexes']
                val = {'base': indexes[0], 'indexes': indexes[1:]}
        elif isinstance(val, dict) and genome_build in val:
            val = _indexes_to_secondary_files(val, genome_build)
        out[refname] = val
    return out