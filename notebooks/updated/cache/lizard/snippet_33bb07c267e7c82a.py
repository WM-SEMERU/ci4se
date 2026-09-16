def predict_from_variants(self, variants, transcript_expression_dict=None,
    gene_expression_dict=None):
    variants = apply_variant_expression_filters(variants,
        transcript_expression_dict=transcript_expression_dict,
        transcript_expression_threshold=self.min_transcript_expression,
        gene_expression_dict=gene_expression_dict,
        gene_expression_threshold=self.min_gene_expression)
    effects = variants.effects(raise_on_error=self.raise_on_error)
    return self.predict_from_mutation_effects(effects=effects,
        transcript_expression_dict=transcript_expression_dict,
        gene_expression_dict=gene_expression_dict)