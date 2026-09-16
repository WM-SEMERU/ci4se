def plot_knee(self):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 8))
    plt.plot(self.x, self.y)
    plt.vlines(self.knee, plt.ylim()[0], plt.ylim()[1])