def homogeneity_score(self, reference_clusters):
    return homogeneity_score(self.get_labels(self), self.get_labels(
        reference_clusters))