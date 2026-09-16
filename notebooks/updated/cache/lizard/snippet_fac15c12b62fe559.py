def notifyBlock(self, queue, blocked):
    if blocked:
        if self.prioritySet[-1] == queue.priority:
            self.prioritySet.pop()
        else:
            pindex = bisect_left(self.prioritySet, queue.priority)
            if pindex < len(self.prioritySet) and self.prioritySet[pindex
                ] == queue.priority:
                del self.prioritySet[pindex]
    elif queue.canPop():
        pindex = bisect_left(self.prioritySet, queue.priority)
        if pindex >= len(self.prioritySet) or self.prioritySet[pindex
            ] != queue.priority:
            self.prioritySet.insert(pindex, queue.priority)
    newblocked = not self.canPop()
    if newblocked != self.blocked:
        self.blocked = newblocked
        if self.parent is not None:
            self.parent.notifyBlock(self, newblocked)