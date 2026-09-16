def _displayFeatures(self, fig, features, minX, maxX, offsetAdjuster):
    labels = []
    for index, feature in enumerate(features):
        fig.plot([offsetAdjuster(feature.start), offsetAdjuster(feature.end
            )], [index * -0.2, index * -0.2], color=feature.color, linewidth=2)
        labels.append(feature.legendLabel())
    fig.axis([minX, maxX, (len(features) + 1) * -0.2, 0.2])
    if labels:
        box = fig.get_position()
        fig.set_position([box.x0, box.y0, box.width, box.height * 0.2])
        fig.legend(labels, loc='lower center', bbox_to_anchor=(0.5, 1.4),
            fancybox=True, shadow=True, ncol=2)