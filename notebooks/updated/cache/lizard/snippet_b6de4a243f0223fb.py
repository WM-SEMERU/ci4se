def solidity_library_symbol(library_name):
    length = min(len(library_name), 36)
    library_piece = library_name[:length]
    hold_piece = '_' * (36 - length)
    return '__{library}{hold}__'.format(library=library_piece, hold=hold_piece)