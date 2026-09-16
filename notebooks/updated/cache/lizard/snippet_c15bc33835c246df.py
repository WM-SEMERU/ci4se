def reconstruct(self, X):
    return self.sess.run(self.x_reconstr_mean, feed_dict={self.x: X})