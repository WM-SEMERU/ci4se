def vcfutilsConsensus(outFile, vcfFile, id_, _, executor):
    executor.execute(
        'vcfutils.pl vcf2fq < %s | filter-fasta.py --fastq --quiet --saveAs fasta --idLambda \'lambda id: "%s"\' > %s'
         % (vcfFile, id_, outFile))