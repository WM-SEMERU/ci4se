def fromgroups(args):
    from jcvi.formats.bed import Bed
    p = OptionParser(fromgroups.__doc__)
    opts, args = p.parse_args(args)
    if len(args) < 2:
        sys.exit(not p.print_help())
    groupsfile = args[0]
    bedfiles = args[1:]
    beds = [Bed(x) for x in bedfiles]
    fp = open(groupsfile)
    groups = [row.strip().split(',') for row in fp]
    for b1, b2 in product(beds, repeat=2):
        extract_pairs(b1, b2, groups)