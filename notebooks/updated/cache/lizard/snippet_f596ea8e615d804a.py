def to_dataframe(self):
    variant_properties = ['contig', 'start', 'ref', 'alt', 'is_snv',
        'is_transversion', 'is_transition']

    def row_from_effect(effect):
        row = OrderedDict()
        row['variant'] = str(effect.variant.short_description)
        for field_name in variant_properties:
            row[field_name] = getattr(effect.variant, field_name, None)
        row['gene_id'] = effect.gene_id
        row['gene_name'] = effect.gene_name
        row['transcript_id'] = effect.transcript_id
        row['transcript_name'] = effect.transcript_name
        row['effect_type'] = effect.__class__.__name__
        row['effect'] = effect.short_description
        return row
    return pd.DataFrame.from_records([row_from_effect(effect) for effect in
        self])