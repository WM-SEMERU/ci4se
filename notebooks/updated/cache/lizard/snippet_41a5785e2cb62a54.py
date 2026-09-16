def unload(self, keepables=None):
    to_del = [ds_id for ds_id, projectable in self.datasets.items() if 
        ds_id not in self.wishlist and (not keepables or ds_id not in
        keepables)]
    for ds_id in to_del:
        LOG.debug('Unloading dataset: %r', ds_id)
        del self.datasets[ds_id]