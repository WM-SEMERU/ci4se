def update(self, docs=None, split=0, parallelism=None, progress_bar=True):
    self.apply(docs=docs, split=split, train=True, clear=False, parallelism
        =parallelism, progress_bar=progress_bar)