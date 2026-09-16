def _summaries(self):
    for var in tf.trainable_variables():
        tf.summary.histogram(var.name, var)
        print(var.name)