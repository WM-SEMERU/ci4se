def MakeOdds(self):
    for hypo, prob in self.Items():
        if prob:
            self.Set(hypo, Odds(prob))
        else:
            self.Remove(hypo)