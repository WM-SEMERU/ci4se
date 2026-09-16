def reset(self):
    self.scores = torch.FloatTensor(torch.FloatStorage())
    self.targets = torch.LongTensor(torch.LongStorage())
    self.weights = torch.FloatTensor(torch.FloatStorage())