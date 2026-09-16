def document_vector(text: str, learn, data, agg: str='mean'):
    s = _tokenizer.tokenizer(text)
    t = torch.tensor(data.vocab.numericalize(s), requires_grad=False).to(device
        )
    m = learn.model[0].encoder.to(device)
    res = m(t).cpu().detach().numpy()
    if agg == 'mean':
        res = res.mean(0)
    elif agg == 'sum':
        res = res.sum(0)
    else:
        raise ValueError('Aggregate by mean or sum')
    return res