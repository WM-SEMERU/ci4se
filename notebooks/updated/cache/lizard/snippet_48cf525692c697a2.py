def runGenome(bfile, options):
    outPrefix = options.out + '.genome'
    if options.sge:
        plinkCommand = ['plink', '--noweb', '--bfile', bfile, '--freq',
            '--out', options.out + '.frequency']
        runCommand(plinkCommand)
        nbJob = splitFile(bfile + '.fam', options.line_per_file_for_sge,
            outPrefix)
        runGenomeSGE(bfile, options.out + '.frequency.frq', nbJob,
            outPrefix, options)
        mergeGenomeLogFiles(outPrefix, nbJob)
    else:
        plinkCommand = ['plink', '--noweb', '--bfile', bfile, '--genome',
            '--genome-full', '--out', outPrefix]
        runCommand(plinkCommand)
    return outPrefix + '.genome'