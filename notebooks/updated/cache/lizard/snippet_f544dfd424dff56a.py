def checkNewCheckpointsAreLeafVertices(self):
    roots = self.getRootJobs()
    jobs = set()
    list(map(lambda x: x._dfs(jobs), roots))
    for y in [x for x in jobs if x.checkpoint]:
        if y not in roots:
            if not Job._isLeafVertex(y):
                raise JobGraphDeadlockException(
                    'New checkpoint job %s is not a leaf in the job graph' % y)