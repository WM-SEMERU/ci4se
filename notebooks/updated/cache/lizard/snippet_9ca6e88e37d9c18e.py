def get_go2obj(self, goids):
    goids = goids.intersection(self.go2obj.keys())
    if len(goids) != len(goids):
        goids_missing = goids.difference(goids)
        print('  {N} MISSING GO IDs: {GOs}'.format(N=len(goids_missing),
            GOs=goids_missing))
    return {go: self.go2obj[go] for go in goids}