def apply_effect_expression_filters(effects, gene_expression_dict,
    gene_expression_threshold, transcript_expression_dict,
    transcript_expression_threshold):
    if gene_expression_dict:
        effects = apply_filter(lambda effect: gene_expression_dict.get(
            effect.gene_id, 0.0) >= gene_expression_threshold, effects,
            result_fn=effects.clone_with_new_elements, filter_name=
            'Effect gene expression (min = %0.4f)' % gene_expression_threshold)
    if transcript_expression_dict:
        effects = apply_filter(lambda effect: transcript_expression_dict.
            get(effect.transcript_id, 0.0) >=
            transcript_expression_threshold, effects, result_fn=effects.
            clone_with_new_elements, filter_name=
            'Effect transcript expression (min=%0.4f)' % (
            transcript_expression_threshold,))
    return effects