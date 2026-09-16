def nextKey(self, key):
    ans = self.nextNode(key)
    return ans.key if ans is not None else None