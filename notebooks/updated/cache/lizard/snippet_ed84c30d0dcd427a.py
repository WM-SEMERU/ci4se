def push(self, item, priority=None):
    priority = item if priority is None else priority
    node = PriorityQueueNode(item, priority)
    for index, current in enumerate(self.priority_queue_list):
        if current.priority < node.priority:
            self.priority_queue_list.insert(index, node)
            return
    self.priority_queue_list.append(node)