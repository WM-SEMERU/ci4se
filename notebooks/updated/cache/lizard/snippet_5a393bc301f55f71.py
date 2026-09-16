def deleterious_permutation(obs_del, context_counts, context_to_mut,
    seq_context, gene_seq, num_permutations=10000, stop_criteria=100,
    pseudo_count=0, max_batch=25000):
    mycontexts = context_counts.index.tolist()
    somatic_base = [base for one_context in mycontexts for base in
        context_to_mut[one_context]]
    max_batch = min(num_permutations, max_batch)
    num_batches = num_permutations // max_batch
    remainder = num_permutations % max_batch
    batch_sizes = [max_batch] * num_batches
    if remainder:
        batch_sizes += [remainder]
    num_sim = 0
    null_del_ct = 0
    for j, batch_size in enumerate(batch_sizes):
        if null_del_ct >= stop_criteria:
            break
        tmp_contxt_pos = seq_context.random_pos(context_counts.iteritems(),
            batch_size)
        tmp_mut_pos = np.hstack(pos_array for base, pos_array in tmp_contxt_pos
            )
        for i, row in enumerate(tmp_mut_pos):
            tmp_mut_info = mc.get_aa_mut_info(row, somatic_base, gene_seq)
            tmp_del_count = cutils.calc_deleterious_info(tmp_mut_info[
                'Reference AA'], tmp_mut_info['Somatic AA'], tmp_mut_info[
                'Codon Pos'])
            if tmp_del_count >= obs_del:
                null_del_ct += 1
            if null_del_ct >= stop_criteria:
                break
        num_sim += i + 1
    del_pval = float(null_del_ct) / num_sim
    return del_pval