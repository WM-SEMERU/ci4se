def preprocess_dataset(dataset, transform, num_workers=8):
    worker_fn = partial(_worker_fn, transform=transform)
    start = time.time()
    pool = mp.Pool(num_workers)
    dataset_transform = []
    dataset_len = []
    for data in pool.map(worker_fn, dataset):
        if data:
            for _data in data:
                dataset_transform.append(_data[:-1])
                dataset_len.append(_data[-1])
    dataset = SimpleDataset(dataset_transform).transform(lambda x: (x[0], x
        [1], x[2], x[3], x[4], x[5]))
    end = time.time()
    pool.close()
    print('Done! Transform dataset costs %.2f seconds.' % (end - start))
    return dataset, dataset_len