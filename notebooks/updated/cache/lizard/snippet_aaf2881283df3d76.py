def run_genesippr(self):
    GeneSippr(args=self, pipelinecommit=self.commit, startingtime=self.
        starttime, scriptpath=self.homepath, analysistype='genesippr',
        cutoff=0.95, pipeline=False, revbait=False)