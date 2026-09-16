def plot(self):
    width = 10
    height = width / 1.618
    f = plt.figure(figsize=(width, height))
    ax = f.add_subplot(111, projection='3d')
    self.plot_state_histogram(ax)
    return f