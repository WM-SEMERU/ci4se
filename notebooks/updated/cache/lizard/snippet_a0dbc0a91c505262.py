def context_chunks(self, context):
    N_chunks = len(self.contexts[context])
    chunks = []
    for j in xrange(N_chunks):
        chunks.append(self.context_chunk(context, j))
    return chunks