def plotAAClusters(sequence, propertyNames, showLines=True, showFigure=True):
    MISSING_AA_VALUE = 0
    propertyClusters = clustersForSequence(sequence, propertyNames,
        missingAAValue=MISSING_AA_VALUE)
    if showFigure:
        minCluster = 1
        maxCluster = -1
        legend = []
        x = np.arange(0, len(sequence))
        plot = plt.plot if showLines else plt.scatter
        for index, propertyName in enumerate(propertyClusters):
            color = TABLEAU20[index]
            clusterNumbers = propertyClusters[propertyName]
            plot(x, clusterNumbers, color=color)
            legend.append(patches.Patch(color=color, label=propertyName))
            propertyMinCluster = min(clusterNumbers)
            if propertyMinCluster < minCluster:
                minCluster = propertyMinCluster
            propertyMaxCluster = max(clusterNumbers)
            if propertyMaxCluster > maxCluster:
                maxCluster = propertyMaxCluster
        plt.legend(handles=legend, loc=(0, 1.1))
        plt.xlim(-0.2, len(sequence) - 0.8)
        plt.ylim(minCluster - 0.5, maxCluster + 0.5)
        plt.yticks(range(maxCluster + 1))
        plt.xlabel('Sequence index')
        plt.ylabel('Property cluster number')
        plt.title(sequence.id)
        plt.show()
    return propertyClusters