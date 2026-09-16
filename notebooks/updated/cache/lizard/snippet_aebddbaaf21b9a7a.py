def _multiply(self, x1, x2, out):
    np.multiply(x1.data, x2.data, out=out.data)