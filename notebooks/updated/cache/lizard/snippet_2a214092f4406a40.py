def referenceLengths(self):
    result = {}
    with samfile(self.filename) as sam:
        if self.referenceIds:
            for referenceId in self.referenceIds:
                tid = sam.get_tid(referenceId)
                if tid == -1:
                    raise UnknownReference(
                        'Reference %r is not present in the SAM/BAM file.' %
                        referenceId)
                else:
                    result[referenceId] = sam.lengths[tid]
        else:
            result = dict(zip(sam.references, sam.lengths))
    return result