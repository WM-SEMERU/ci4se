def predict_epitopes_from_args(args):
    mhc_model = mhc_binding_predictor_from_args(args)
    variants = variant_collection_from_args(args)
    gene_expression_dict = rna_gene_expression_dict_from_args(args)
    transcript_expression_dict = rna_transcript_expression_dict_from_args(args)
    predictor = TopiaryPredictor(mhc_model=mhc_model,
        padding_around_mutation=args.padding_around_mutation, ic50_cutoff=
        args.ic50_cutoff, percentile_cutoff=args.percentile_cutoff,
        min_transcript_expression=args.rna_min_transcript_expression,
        min_gene_expression=args.rna_min_gene_expression,
        only_novel_epitopes=args.only_novel_epitopes, raise_on_error=not
        args.skip_variant_errors)
    return predictor.predict_from_variants(variants=variants,
        transcript_expression_dict=transcript_expression_dict,
        gene_expression_dict=gene_expression_dict)