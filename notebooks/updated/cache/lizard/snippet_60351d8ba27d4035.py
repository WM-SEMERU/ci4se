def evaluate(dataloader_eval, metric):
    metric.reset()
    for _, seqs in enumerate(dataloader_eval):
        input_ids, valid_len, type_ids, label = seqs
        out = model(input_ids.as_in_context(ctx), type_ids.as_in_context(
            ctx), valid_len.astype('float32').as_in_context(ctx))
        metric.update([label], [out])
    metric_nm, metric_val = metric.get()
    if not isinstance(metric_nm, list):
        metric_nm = [metric_nm]
        metric_val = [metric_val]
    metric_str = 'validation metrics:' + ','.join([(i + ':%.4f') for i in
        metric_nm])
    logging.info(metric_str, *metric_val)