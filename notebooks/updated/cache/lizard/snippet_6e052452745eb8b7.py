def fit(self, train_set, test_set):
    with tf.Graph().as_default(), tf.Session() as self.tf_session:
        self.build_model()
        tf.global_variables_initializer().run()
        third = self.num_epochs // 3
        for i in range(self.num_epochs):
            lr_decay = self.lr_decay ** max(i - third, 0.0)
            self.tf_session.run(tf.assign(self.lr_var, tf.multiply(self.
                learning_rate, lr_decay)))
            train_perplexity = self._run_train_step(train_set, 'train')
            print('Epoch: %d Train Perplexity: %.3f' % (i + 1,
                train_perplexity))
        test_perplexity = self._run_train_step(test_set, 'test')
        print('Test Perplexity: %.3f' % test_perplexity)