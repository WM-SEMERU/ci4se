def push(self, record, shard):
    heapq.heappush(self.heap, heap_item(self.clock, record, shard))