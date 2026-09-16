def forward(self, X):
    return self.W(X).sum(dim=1) + self.b