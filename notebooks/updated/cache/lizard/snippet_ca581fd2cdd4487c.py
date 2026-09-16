def continuous_eval_on_train_data(self):
    for ckpt_path in next_checkpoint(self._hparams.model_dir, self._hparams
        .eval_timeout_mins):
        train_step = decoding.get_step_from_ckpt_path(ckpt_path)
        if train_step == 0:
            tf.logging.info('Skipping evaluation at step 0')
            continue
        self.evaluate_on_train_data()