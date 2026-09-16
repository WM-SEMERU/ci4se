def import_tf_tensor(self, x, tf_x):
    return self.LaidOutTensor(self.make_slices(tf_x, x.shape))