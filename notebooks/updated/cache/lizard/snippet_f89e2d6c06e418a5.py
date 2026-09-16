def run_postdecode_hooks(decode_hook_args, dataset_split):
    hooks = decode_hook_args.problem.decode_hooks
    if not hooks:
        return
    global_step = latest_checkpoint_step(decode_hook_args.estimator.model_dir)
    if global_step is None:
        tf.logging.info(
            'Skipping decode hooks because no checkpoint yet available.')
        return
    tf.logging.info('Running decode hooks.')
    parent_dir = os.path.join(decode_hook_args.output_dirs[0], os.pardir)
    child_dir = decode_hook_args.decode_hparams.summaries_log_dir
    if dataset_split is not None:
        child_dir += '_{}'.format(dataset_split)
    final_dir = os.path.join(parent_dir, child_dir)
    summary_writer = tf.summary.FileWriter(final_dir)
    for hook in hooks:
        with tf.Graph().as_default():
            summaries = hook(decode_hook_args)
        if summaries:
            summary = tf.Summary(value=list(summaries))
            summary_writer.add_summary(summary, global_step)
    summary_writer.close()
    tf.logging.info('Decode hooks done.')