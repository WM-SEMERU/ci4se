def train(self):
    self.stamp_start = time.time()
    for iteration, batch in tqdm.tqdm(enumerate(self.iter_train), desc=
        'train', total=self.max_iter, ncols=80):
        self.epoch = self.iter_train.epoch
        self.iteration = iteration
        if (self.interval_validate and self.iteration % self.
            interval_validate == 0):
            self.validate()
        batch = map(datasets.transform_lsvrc2012_vgg16, batch)
        in_vars = utils.batch_to_vars(batch, device=self.device)
        self.model.zerograds()
        loss = self.model(*in_vars)
        if loss is not None:
            loss.backward()
            self.optimizer.update()
            lbl_true = zip(*batch)[1]
            lbl_pred = chainer.functions.argmax(self.model.score, axis=1)
            lbl_pred = chainer.cuda.to_cpu(lbl_pred.data)
            acc = utils.label_accuracy_score(lbl_true, lbl_pred, self.model
                .n_class)
            self._write_log(**{'epoch': self.epoch, 'iteration': self.
                iteration, 'elapsed_time': time.time() - self.stamp_start,
                'train/loss': float(loss.data), 'train/acc': acc[0],
                'train/acc_cls': acc[1], 'train/mean_iu': acc[2],
                'train/fwavacc': acc[3]})
        if iteration >= self.max_iter:
            self._save_model()
            break