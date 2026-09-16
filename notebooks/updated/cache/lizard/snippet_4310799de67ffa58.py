def evaluate(data_source, batch_size, ctx=None):
    total_L = 0
    hidden = cache_cell.begin_state(func=mx.nd.zeros, batch_size=batch_size,
        ctx=context[0])
    next_word_history = None
    cache_history = None
    for i in range(0, len(data_source) - 1, args.bptt):
        if i > 0:
            print('Batch %d/%d, ppl %f' % (i, len(data_source), math.exp(
                total_L / i)))
        data, target = get_batch(data_source, i)
        data = data.as_in_context(ctx)
        target = target.as_in_context(ctx)
        L = 0
        outs, next_word_history, cache_history, hidden = cache_cell(data,
            target, next_word_history, cache_history, hidden)
        for out in outs:
            L += (-mx.nd.log(out)).asscalar()
        total_L += L / data.shape[1]
        hidden = detach(hidden)
    return total_L / len(data_source)