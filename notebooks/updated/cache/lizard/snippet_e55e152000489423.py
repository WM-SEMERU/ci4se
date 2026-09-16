def infer_transportation_mode(self, clf, min_time):
    self.transportation_modes = speed_clustering(clf, self.points, min_time)
    return self