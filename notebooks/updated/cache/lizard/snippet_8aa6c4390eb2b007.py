def _stats(arr, percentiles=(2, 98), **kwargs):
    sample, edges = np.histogram(arr[~arr.mask], **kwargs)
    return {'pc': np.percentile(arr[~arr.mask], percentiles).astype(arr.
        dtype).tolist(), 'min': arr.min().item(), 'max': arr.max().item(),
        'std': arr.std().item(), 'histogram': [sample.tolist(), edges.tolist()]
        }