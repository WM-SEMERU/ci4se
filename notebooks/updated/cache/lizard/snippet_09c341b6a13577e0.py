def com_find2D(ar_grid, **kwargs):
    b_reorder = True
    b_oneOffset = True
    for key, value in kwargs.iteritems():
        if key == 'ordering' and value == 'rc':
            b_reorder = False
        if key == 'ordering' and value == 'xy':
            b_reorder = True
        if key == 'indexing' and value == 'zero':
            b_oneOffset = False
        if key == 'indexing' and value == 'one':
            b_oneOffset = True
    f_Smass = ar_grid.sum()
    f_comX = (ar_grid[nonzero(ar_grid)] * (nonzero(ar_grid)[1] + 1)).sum(
        ) / f_Smass
    f_comY = (ar_grid[nonzero(ar_grid)] * (nonzero(ar_grid)[0] + 1)).sum(
        ) / f_Smass
    if b_reorder:
        ar_ret = array((f_comX, f_comY))
    if not b_reorder:
        ar_ret = array((f_comY, f_comX))
    if not b_oneOffset:
        ar_ret -= 1.0
    return ar_ret