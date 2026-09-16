def sampleCellsWithinColumns(numCellPairs, cellsPerColumn, numColumns, seed=42
    ):
    np.random.seed(seed)
    cellPairs = []
    for i in range(numCellPairs):
        randCol = np.random.randint(numColumns)
        randCells = np.random.choice(np.arange(cellsPerColumn), (2,),
            replace=False)
        cellsPair = randCol * cellsPerColumn + randCells
        cellPairs.append(cellsPair)
    return cellPairs