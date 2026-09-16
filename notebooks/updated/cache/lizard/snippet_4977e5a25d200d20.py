def get_fscore(self, fmap=''):
    trees = self.get_dump(fmap)
    fmap = {}
    for tree in trees:
        for line in tree.split('\n'):
            arr = line.split('[')
            if len(arr) == 1:
                continue
            fid = arr[1].split(']')[0]
            fid = fid.split('<')[0]
            if fid not in fmap:
                fmap[fid] = 1
            else:
                fmap[fid] += 1
    return fmap