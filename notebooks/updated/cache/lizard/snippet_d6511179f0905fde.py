def chunkReceived(self, who, chunkNumber, chunkData):

    def verifyError(error):
        error.trap(VerifyError)
        self.nexus.decreaseScore(who, self.authorities)
    return self.nexus.verifyChunk(self.name, who, chunkNumber, sha.new(
        chunkData).digest(), self.authorities).addCallbacks(lambda whatever:
        self.chunkVerified(who, chunkNumber, chunkData), verifyError)