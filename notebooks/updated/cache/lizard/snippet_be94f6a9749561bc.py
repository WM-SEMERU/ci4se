def run_forward_backward(self, batch: mx.io.DataBatch, metric: mx.metric.
    EvalMetric):
    self.module.forward_backward(batch)
    self.module.update_metric(metric, batch.label)