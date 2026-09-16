def plot_confusion_matrix(self, normalised=True):
    conf_matrix = self.confusion_matrix()
    if normalised:
        sns.heatmap(conf_matrix, annot=True, annot_kws={'size': 12}, fmt=
            '2.1f', cmap='YlGnBu', vmin=0.0, vmax=100.0, xticklabels=list(
            self.class_dictionary.keys()), yticklabels=self.truth_classes)
    else:
        sns.heatmap(self.pixel_classification_counts, annot=True, annot_kws
            ={'size': 12}, fmt='2.1f', cmap='YlGnBu', vmin=0.0, vmax=np.max
            (self.pixel_classification_counts), xticklabels=list(self.
            class_dictionary.keys()), yticklabels=self.truth_classes)