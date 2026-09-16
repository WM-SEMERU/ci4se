def worker_loop_v1(dataset, key_queue, data_queue, batchify_fn):
    while True:
        idx, samples = key_queue.get()
        if idx is None:
            break
        batch = batchify_fn([dataset[i] for i in samples])
        data_queue.put((idx, batch))