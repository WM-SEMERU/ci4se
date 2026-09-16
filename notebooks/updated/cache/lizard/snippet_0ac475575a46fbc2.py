def _refine_j(seq, species):
    jgerm = germlines.get_germline(seq['j_gene']['full'], species)
    aln = global_alignment(seq['vdj_nt'], jgerm)
    append = ''
    for s, g in zip(aln.aligned_query[::-1], aln.aligned_target[::-1]):
        if s != '-':
            break
        else:
            append += g
    seq['vdj_nt'] = seq['vdj_nt'] + append[::-1]