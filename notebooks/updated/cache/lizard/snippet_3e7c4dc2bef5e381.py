def add_rna_args(parser, min_mapping_quality_default=MIN_READ_MAPPING_QUALITY):
    rna_group = parser.add_argument_group('RNA')
    rna_group.add_argument('--bam', required=True, help=
        'BAM file containing RNAseq reads')
    rna_group.add_argument('--min-mapping-quality', type=int, default=
        min_mapping_quality_default, help=
        'Minimum MAPQ value to allow for a read (default %(default)s)')
    rna_group.add_argument('--use-duplicate-reads', default=False, action=
        'store_true')
    rna_group.add_argument('--drop-secondary-alignments', default=False,
        action='store_true')
    return rna_group