def _index_to_ansi_values(self, index):
    if self.__class__.__name__[0] == 'F':
        if index < 8:
            index += ANSI_FG_LO_BASE
        else:
            index += ANSI_FG_HI_BASE - 8
    elif index < 8:
        index += ANSI_BG_LO_BASE
    else:
        index += ANSI_BG_HI_BASE - 8
    return [str(index)]