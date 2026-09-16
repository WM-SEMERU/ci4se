def PhyDMSPrepAlignmentParser():
    parser = ArgumentParserNoArgHelp(formatter_class=
        ArgumentDefaultsRawDescriptionFormatter, description='\n'.join([
        """Prepare alignment of protein-coding DNA sequences.
""", 'Steps:',
        " * Any sequences specified by '--purgeseqs' are removed.",
        ' * Sequences not of length divisible by 3 are removed.',
        ' * Sequences with ambiguous nucleotides are removed.',
        ' * Sequences with non-terminal stop codons are removed;',
        '   terminal stop codons are trimmed.',
        ' * Sequences that do not encode unique proteins are removed',
        "   unless they are specified for retention by '--keepseqs'.",
        ' * A multiple sequence alignment is built using MAFFT.',
        "   This step is skipped if you specify '--prealigned'.",
        ' * Sites gapped in reference sequence are stripped.',
        ' * Sequences with too little protein identity to reference',
        '   sequence are removed, counting both mismatches and unstripped',
        "   gaps as differences. Identity cutoff set by '--minidentity'.",
        ' * Sequences too similar to other sequences are removed. An',
        '   effort is made to keep one representative of sequences found',
        '   many times in input set. Uniqueness threshold set ',
        "   by '--minuniqueness'. You can specify sequences to not",
        "   remove via '--keepseqs'.",
        ' * Problematic characters in header names are replaced by',
        '   underscores. This is any space, comma, colon, semicolon',
        '   parenthesis, bracket, single quote, or double quote.',
        ' * An alignment is written, as well as a plot with same root',
        "   but extension '.pdf' that shows divergence from reference",
        '   of all sequences retained and purged due to identity or',
        '   uniqueness.\n', phydmslib.__acknowledgments__, 'Version {0}'.
        format(phydmslib.__version__), 'Full documentation at {0}'.format(
        phydmslib.__url__)]))
    parser.add_argument('inseqs', type=ExistingFile, help=
        'FASTA file giving input coding sequences.')
    parser.add_argument('alignment', help=
        "Name of created output FASTA alignment. PDF plot has same root, but extension '.pdf'."
        )
    parser.add_argument('refseq', help=
        "Reference sequence in 'inseqs': specify substring found ONLY in header for that sequence."
        )
    parser.set_defaults(prealigned=False)
    parser.add_argument('--prealigned', action='store_true', dest=
        'prealigned', help=
        "Sequences in 'inseqs' are already aligned, do NOT re-align.")
    parser.add_argument('--mafft', help=
        'Path to MAFFT (http://mafft.cbrc.jp/alignment/software/).',
        default='mafft')
    parser.add_argument('--minidentity', type=FloatBetweenZeroAndOne, help=
        "Purge sequences with <= this protein identity to 'refseq'.",
        default=0.7)
    parser.add_argument('--minuniqueness', type=IntGreaterThanZero, default
        =2, help=
        'Require each sequence to have >= this many protein differences relative to other sequences.'
        )
    parser.add_argument('--purgeseqs', nargs='*', help=
        'Specify sequences to always purge. Any sequences with any of the substrings specified here are always removed. The substrings can either be passed as repeated arguments here, or as the name of an existing file which has one substring per line.'
        )
    parser.add_argument('--keepseqs', nargs='*', help=
        "Do not purge any of these sequences for lack of identity or uniqueness. Specified in the same fashion as for '--purgeseqs'."
        )
    parser.add_argument('-v', '--version', action='version', version=
        '%(prog)s {version}'.format(version=phydmslib.__version__))
    return parser