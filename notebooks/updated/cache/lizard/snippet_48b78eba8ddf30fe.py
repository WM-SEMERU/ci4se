def distincts(self, nested=False):
    argpairs = self._argdistincts(absolute=True)
    left = argpairs._content['0']
    right = argpairs._content['1']
    out = self.JaggedArray.fromoffsets(argpairs.offsets, self.Table.named(
        'tuple', self._content[left], self._content[right]).flattentuple())
    out._parents = argpairs._parents
    if nested:
        out = self.JaggedArray.fromcounts(self.numpy.maximum(0, self.counts -
            1), self.JaggedArray.fromcounts(self.index[:, :0:-1].flatten(),
            out._content))
    return out