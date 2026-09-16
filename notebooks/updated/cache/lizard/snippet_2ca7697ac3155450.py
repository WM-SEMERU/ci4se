def runExperiment():
    trainSeqN = [5, 10, 20, 50, 100, 200]
    rptPerCondition = 20
    correctRateAll = np.zeros((len(trainSeqN), rptPerCondition))
    missRateAll = np.zeros((len(trainSeqN), rptPerCondition))
    fpRateAll = np.zeros((len(trainSeqN), rptPerCondition))
    for i in xrange(len(trainSeqN)):
        for rpt in xrange(rptPerCondition):
            numTrainSequence = trainSeqN[i]
            correctRate, missRate, fpRate = runSingleExperiment(
                numTrainSequence=numTrainSequence)
            correctRateAll[i, rpt] = correctRate
            missRateAll[i, rpt] = missRate
            fpRateAll[i, rpt] = fpRate
    plt.figure()
    plt.subplot(2, 2, 1)
    plt.semilogx(trainSeqN, 100 * np.mean(correctRateAll, 1), '-*')
    plt.xlabel(' Training Sequence Number')
    plt.ylabel(' Hit Rate - Best Match (%)')
    plt.subplot(2, 2, 2)
    plt.semilogx(trainSeqN, 100 * np.mean(missRateAll, 1), '-*')
    plt.xlabel(' Training Sequence Number')
    plt.ylabel(' Miss Rate (%)')
    plt.subplot(2, 2, 3)
    plt.semilogx(trainSeqN, 100 * np.mean(fpRateAll, 1), '-*')
    plt.xlabel(' Training Sequence Number')
    plt.ylabel(' False Positive Rate (%)')
    plt.savefig('result/ReberSequence_HMMperformance.pdf')
    plt.show()