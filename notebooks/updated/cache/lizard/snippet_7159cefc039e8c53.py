def getLeastUsedCell(self, c):
    segmentsPerCell = numpy.zeros(self.cellsPerColumn, dtype='uint32')
    for i in range(self.cellsPerColumn):
        segmentsPerCell[i] = self.getNumSegmentsInCell(c, i)
    cellMinUsage = numpy.where(segmentsPerCell == segmentsPerCell.min())[0]
    self._random.getUInt32(len(cellMinUsage))
    return cellMinUsage[self._random.getUInt32(len(cellMinUsage))]