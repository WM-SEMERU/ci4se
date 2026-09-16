def gen_batches(data, batch_size):
    data = np.array(data)
    for i in range(0, data.shape[0], batch_size):
        yield data[i:i + batch_size]