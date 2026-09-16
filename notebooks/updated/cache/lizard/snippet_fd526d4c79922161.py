def copy(self):
    features_copy = [feature.copy() for feature in self.features]
    copy = type(self)(self.top.seq, circular=self.circular, features=
        features_copy, name=self.name, bottom=self.bottom.seq, run_checks=False
        )
    return copy