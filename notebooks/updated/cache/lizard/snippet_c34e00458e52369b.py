def atlas_peer_dequeue_all(peer_queue=None):
    peers = []
    with AtlasPeerQueueLocked(peer_queue) as pq:
        while len(pq) > 0:
            peers.append(pq.pop(0))
    return peers