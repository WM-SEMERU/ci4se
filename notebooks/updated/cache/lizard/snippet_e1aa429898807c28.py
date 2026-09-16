def evaluation_step(self, Xi, training=False):
    with torch.set_grad_enabled(training):
        self.module_.train(training)
        return self.infer(Xi)