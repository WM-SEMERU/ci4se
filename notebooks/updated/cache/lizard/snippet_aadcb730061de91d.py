def check(fastaFile, jsonFiles):
    reads = FastaReads(fastaFile)
    readsAlignments = BlastReadsAlignments(reads, jsonFiles)
    for index, readAlignments in enumerate(readsAlignments):
        fastaLen = len(readAlignments.read)
        for readAlignment in readAlignments:
            for hsp in readAlignment.hsps:
                assert fastaLen >= len(hsp.query) - hsp.query.count('-'
                    ), """record %d: FASTA len %d < HSP query len %d.
FASTA: %s
Query match: %s""" % (
                    index, fastaLen, len(hsp.query), readAlignments.read.
                    sequence, hsp.query)
                assert fastaLen >= hsp.readEnd >= hsp.readStart, """record %d: FASTA len %d not greater than both read offsets (%d - %d), or read offsets are non-increasing. FASTA: %s
Query match: %s""" % (
                    index, fastaLen, hsp.readStart, hsp.readEnd,
                    readAlignments.read.sequence, hsp.query)