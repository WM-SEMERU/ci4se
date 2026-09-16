def protein_sequences_generator_to_dataframe(
    variant_and_protein_sequences_generator):
    return dataframe_from_generator(element_class=ProteinSequence,
        variant_and_elements_generator=
        variant_and_protein_sequences_generator, converters=dict(gene=lambda
        x: ';'.join(x)))