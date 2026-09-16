def transform(self, X=None, y=None):
    translation_x, translation_y = self.translation
    translation_matrix = np.array([[1, 0, translation_x], [0, 1,
        translation_y]])
    self.tx.set_parameters(translation_matrix)
    if self.lazy or X is None:
        return self.tx
    else:
        return self.tx.apply_to_image(X, reference=self.reference)