def liftover(pass_pos, matures):
    fixed_pos = []
    _print_header(pass_pos)
    for pos in pass_pos:
        mir = pos['mature']
        db_pos = matures[pos['chrom']]
        mut = _parse_mut(pos['sv'])
        print([db_pos[mir], mut, pos['sv']])
        pos['pre_pos'] = db_pos[mir][0] + mut[1] - 1
        pos['nt'] = list(mut[0])
        fixed_pos.append(pos)
        print_vcf(pos)
    return fixed_pos