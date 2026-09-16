def on_validation_batch_end(self):
    for callback in self.callbacks:
        callback.on_validation_batch_end(self)
    self.epoch_info.result_accumulator.calculate(self)