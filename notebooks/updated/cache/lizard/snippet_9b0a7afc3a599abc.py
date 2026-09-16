def randomizeSequence(sequence, symbolsPerSequence, numColumns, sparsity, p
    =0.25):
    randomizedSequence = []
    sparseCols = int(numColumns * sparsity)
    numSymbolsToChange = int(symbolsPerSequence * p)
    symIndices = np.random.permutation(np.arange(symbolsPerSequence))
    for symbol in range(symbolsPerSequence):
        randomizedSequence.append(sequence[symbol])
    i = 0
    while numSymbolsToChange > 0:
        randomizedSequence[symIndices[i]] = generateRandomSymbol(numColumns,
            sparseCols)
        i += 1
        numSymbolsToChange -= 1
    return randomizedSequence