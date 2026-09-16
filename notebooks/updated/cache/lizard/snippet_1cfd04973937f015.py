def getGrid(self, use_mask=True):
    grid_card_name = 'WATERSHED_MASK'
    if not use_mask:
        grid_card_name = 'ELEVATION'
    return self.getGridByCard(grid_card_name)