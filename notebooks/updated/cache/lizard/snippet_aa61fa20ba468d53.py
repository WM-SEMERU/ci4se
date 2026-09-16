def train(self, data_iterator):
    optimizer = get_optimizer(self.master_optimizer)
    self.model = model_from_yaml(self.yaml, self.custom_objects)
    self.model.compile(optimizer=optimizer, loss=self.master_loss, metrics=
        self.master_metrics)
    self.model.set_weights(self.parameters.value)
    feature_iterator, label_iterator = tee(data_iterator, 2)
    x_train = np.asarray([x for x, y in feature_iterator])
    y_train = np.asarray([y for x, y in label_iterator])
    self.model.compile(optimizer=self.master_optimizer, loss=self.
        master_loss, metrics=self.master_metrics)
    weights_before_training = self.model.get_weights()
    if x_train.shape[0] > self.train_config.get('batch_size'):
        self.model.fit(x_train, y_train, **self.train_config)
    weights_after_training = self.model.get_weights()
    deltas = subtract_params(weights_before_training, weights_after_training)
    yield deltas