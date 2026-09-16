def confusion_matrix(self):
    return plot.confusion_matrix(self.y_true, self.y_pred, self.
        target_names, ax=_gen_ax())