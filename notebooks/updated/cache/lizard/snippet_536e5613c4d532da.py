def load_rnn_checkpoint(cells, prefix, epoch):
    sym, arg, aux = load_checkpoint(prefix, epoch)
    if isinstance(cells, BaseRNNCell):
        cells = [cells]
    for cell in cells:
        arg = cell.pack_weights(arg)
    return sym, arg, aux