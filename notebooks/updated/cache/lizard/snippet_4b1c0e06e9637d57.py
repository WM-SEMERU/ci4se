def get_common_pred(self, pred):
    pred = self.clean_pred(pred)
    common_pred = self.pred2common.get(pred)
    return common_pred