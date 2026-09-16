def calc_true_performance(self, printout=False):
    try:
        self.calc_confusion_matrix(printout=False)
    except DataError as e:
        print(e.msg)
        raise
    if self.TP + self.FP == 0:
        self.precision = np.nan
    else:
        self.precision = self.TP / (self.TP + self.FP)
    if self.TP + self.FN == 0:
        self.recall = np.nan
    else:
        self.recall = self.TP / (self.TP + self.FN)
    if self.precision + self.recall == 0:
        self.F1_measure = np.nan
    else:
        self.F1_measure = 2 * self.precision * self.recall / (self.
            precision + self.recall)
    if printout:
        print('True performance is:')
        print('--------------------')
        print('Precision: {} \t Recall: {} \t F1 measure: {}'.format(self.
            precision, self.recall, self.F1_measure))