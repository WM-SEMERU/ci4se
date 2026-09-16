def check_learns_zero_output_rnn(model, sgd, X, Y, initial_hidden=None):
    outputs, get_dX = model.begin_update(X, initial_hidden)
    Yh, h_n = outputs
    tupleDy = Yh - Y, h_n
    dX = get_dX(tupleDy, sgd=sgd)
    prev = numpy.abs(Yh.sum())
    print(prev)
    for i in range(1000):
        outputs, get_dX = model.begin_update(X)
        Yh, h_n = outputs
        current_sum = numpy.abs(Yh.sum())
        tupleDy = Yh - Y, h_n
        dX = get_dX(tupleDy, sgd=sgd)
    print(current_sum)