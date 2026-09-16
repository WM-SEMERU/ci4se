def addGenotypePhenotypeSearchOptions(parser):
    parser.add_argument('--phenotype_association_set_id', '-s', default=
        None, help=
        'Only return associations from this phenotype_association_set.')
    parser.add_argument('--feature_ids', '-f', default=None, help=
        'Only return associations for these features.')
    parser.add_argument('--phenotype_ids', '-p', default=None, help=
        'Only return associations for these phenotypes.')
    parser.add_argument('--evidence', '-E', default=None, help=
        'Only return associations to this evidence.')