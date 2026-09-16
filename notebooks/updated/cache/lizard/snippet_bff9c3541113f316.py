def log_train(batch_id, batch_num, metric, step_loss, log_interval,
    epoch_id, learning_rate):
    metric_nm, metric_val = metric.get()
    if not isinstance(metric_nm, list):
        metric_nm = [metric_nm]
        metric_val = [metric_val]
    train_str = ('[Epoch %d Batch %d/%d] loss=%.4f, lr=%.7f, metrics:' +
        ','.join([(i + ':%.4f') for i in metric_nm]))
    logging.info(train_str, epoch_id + 1, batch_id + 1, batch_num, 
        step_loss / log_interval, learning_rate, *metric_val)