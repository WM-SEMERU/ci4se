def gene_id_of_associated_transcript(effect):
    return apply_to_transcript_if_exists(effect=effect, fn=lambda t: t.
        gene_id, default=None)