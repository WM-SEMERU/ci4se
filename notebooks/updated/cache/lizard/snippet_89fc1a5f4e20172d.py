def fit_transform(self, X, num_epochs=10, updates_epoch=10,
    stop_param_updates=dict(), batch_size=1, show_progressbar=False,
    show_epoch=False):
    self.fit(X, num_epochs, updates_epoch, stop_param_updates, batch_size,
        show_progressbar, show_epoch)
    return self.transform(X, batch_size=batch_size)