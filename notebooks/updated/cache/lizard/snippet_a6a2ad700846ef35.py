def averaging(grid, numGrid, numPix):
    Nbig = numGrid
    Nsmall = numPix
    small = grid.reshape([int(Nsmall), int(Nbig / Nsmall), int(Nsmall), int
        (Nbig / Nsmall)]).mean(3).mean(1)
    return small