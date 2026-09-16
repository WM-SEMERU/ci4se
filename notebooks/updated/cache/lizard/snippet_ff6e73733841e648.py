def resample_multichan(xs, ann, fs, fs_target, resamp_ann_chan=0):
    assert resamp_ann_chan < xs.shape[1]
    lx = []
    lt = None
    for chan in range(xs.shape[1]):
        resampled_x, resampled_t = resample_sig(xs[:, (chan)], fs, fs_target)
        lx.append(resampled_x)
        if chan == resamp_ann_chan:
            lt = resampled_t
    new_sample = resample_ann(lt, ann.sample)
    assert ann.sample.shape == new_sample.shape
    resampled_ann = Annotation(record_name=ann.record_name, extension=ann.
        extension, sample=new_sample, symbol=ann.symbol, subtype=ann.
        subtype, chan=ann.chan, num=ann.num, aux_note=ann.aux_note, fs=
        fs_target)
    return np.column_stack(lx), resampled_ann