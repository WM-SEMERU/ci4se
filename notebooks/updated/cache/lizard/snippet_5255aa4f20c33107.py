def parseFASTACommandLineOptions(args):
    if not (args.fasta or args.fastq or args.fasta_ss):
        args.fasta = True
    readClass = readClassNameToClass[args.readClass]
    if args.fasta:
        from dark.fasta import FastaReads
        return FastaReads(args.fastaFile, readClass=readClass)
    elif args.fastq:
        from dark.fastq import FastqReads
        return FastqReads(args.fastaFile, readClass=readClass)
    else:
        from dark.fasta_ss import SSFastaReads
        return SSFastaReads(args.fastaFile, readClass=readClass)