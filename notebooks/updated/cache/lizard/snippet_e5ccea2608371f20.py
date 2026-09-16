def filesFromHere_explore(self, astr_startPath='/'):
    self.l_fwd = []
    self.treeExplore(startPath=astr_startPath, f=self.fwd)
    self.l_allFiles = [f.split('/') for f in self.l_fwd]
    for i in range(0, len(self.l_allFiles)):
        self.l_allFiles[i][0] = '/'
    return self.l_fwd