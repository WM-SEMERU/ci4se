def make_variant_sequences_arg_parser(add_sequence_length_arg=False, **kwargs):
    parser = make_rna_reads_arg_parser(**kwargs)
    add_variant_sequence_args(parser=parser, add_sequence_length_arg=
        add_sequence_length_arg)
    return parser