def from_variant_and_transcript(cls, variant, transcript, context_size):
    if not transcript.contains_start_codon:
        logger.info('Expected transcript %s for variant %s to have start codon'
            , transcript.name, variant)
        return None
    if not transcript.contains_stop_codon:
        logger.info('Expected transcript %s for variant %s to have stop codon',
            transcript.name, variant)
        return None
    if not transcript.protein_sequence:
        logger.info(
            'Expected transript %s for variant %s to have protein sequence',
            transcript.name, variant)
        return None
    sequence_key = ReferenceSequenceKey.from_variant_and_transcript(variant
        =variant, transcript=transcript, context_size=context_size)
    if sequence_key is None:
        logger.info('No sequence key for variant %s on transcript %s',
            variant, transcript.name)
        return None
    return cls.from_variant_and_transcript_and_sequence_key(variant=variant,
        transcript=transcript, sequence_key=sequence_key)