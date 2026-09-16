def parseBranches(self, descendants):
    i, branches = self.parseTopDepth(descendants), []
    for descendant in descendants:
        if self.getHeadingLevel(descendant, self.hierarchy) == i:
            branches.append({'source': descendant})
        if self.getHeadingLevel(descendant, self.hierarchy) > i and branches:
            branches[-1].setdefault('descendants', []).append(descendant)
    return [TOC(str(descendant), depth=i, hierarchy=self.hierarchy, **
        branch) for branch in branches]