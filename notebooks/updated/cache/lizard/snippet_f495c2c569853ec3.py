def train_epoch(self, epoch_info: EpochInfo, interactive=True):
    epoch_info.on_epoch_begin()
    if interactive:
        iterator = tqdm.trange(epoch_info.batches_per_epoch, file=sys.
            stdout, desc='Training', unit='batch')
    else:
        iterator = range(epoch_info.batches_per_epoch)
    for batch_idx in iterator:
        batch_info = BatchInfo(epoch_info, batch_idx)
        batch_info.on_batch_begin()
        self.train_batch(batch_info)
        batch_info.on_batch_end()
    epoch_info.result_accumulator.freeze_results()
    epoch_info.on_epoch_end()