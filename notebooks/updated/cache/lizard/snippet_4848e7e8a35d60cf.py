def Print(self):
    for hypo, prob in sorted(self.Items()):
        print(hypo, prob)