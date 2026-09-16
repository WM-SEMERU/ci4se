def add(self, fig, title, minX, maxX, offsetAdjuster=None, sequenceFetcher=None
    ):
    offsetAdjuster = offsetAdjuster or (lambda x: x)
    fig.set_title('Target sequence features', fontsize=self.TITLE_FONTSIZE)
    fig.set_yticks([])
    features = FeatureList(title, self.DATABASE, self.WANTED_TYPES,
        sequenceFetcher=sequenceFetcher)
    if features.offline:
        fig.text(minX + (maxX - minX) / 3.0, 0,
            'You (or Genbank) appear to be offline.', fontsize=self.FONTSIZE)
        fig.axis([minX, maxX, -1, 1])
        return None
    nFeatures = len(features)
    if nFeatures == 0:
        fig.text(0.5, 0.5, 'No features found', horizontalalignment=
            'center', verticalalignment='center', transform=fig.transAxes,
            fontsize=self.FONTSIZE)
        fig.axis([minX, maxX, -1, 1])
    elif nFeatures <= self.MAX_FEATURES_TO_DISPLAY:
        self._displayFeatures(fig, features, minX, maxX, offsetAdjuster)
    else:
        self.tooManyFeaturesToPlot = True
        fig.text(0.5, 0.5, 'Too many features to plot', horizontalalignment
            ='center', verticalalignment='center', fontsize=self.FONTSIZE,
            transform=fig.transAxes)
        fig.axis([minX, maxX, -1, 1])
    return features