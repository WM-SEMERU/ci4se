def get_nowait_from_queue(queue):
    data = []
    for _ in range(queue.qsize()):
        try:
            data.append(queue.get_nowait())
        except q.Empty:
            break
    return data