def data_iterator_simple(load_func, num_examples, batch_size, shuffle=False,
    rng=None, with_memory_cache=True, with_file_cache=True, cache_dir=None,
    epoch_begin_callbacks=[], epoch_end_callbacks=[]):
    return data_iterator(SimpleDataSource(load_func, num_examples, shuffle=
        shuffle, rng=rng), batch_size=batch_size, with_memory_cache=
        with_memory_cache, with_file_cache=with_file_cache, cache_dir=
        cache_dir, epoch_begin_callbacks=epoch_begin_callbacks,
        epoch_end_callbacks=epoch_end_callbacks)