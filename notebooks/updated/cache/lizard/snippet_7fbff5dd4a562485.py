def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, 0, len(heap) - 1)