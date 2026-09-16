def histogram(neuron, feature, ax, bins=15, normed=True, cumulative=False):
    feature_values = nm.get(feature, neuron)
    ax.hist(feature_values, bins=bins, cumulative=cumulative, normed=normed)