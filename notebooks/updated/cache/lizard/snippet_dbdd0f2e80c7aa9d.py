def validate_next(stepper, metrics, val_iter):
    stepper.reset(False)
    with no_grad_context():
        *x, y = val_iter.next()
        preds, l = stepper.evaluate(VV(x), VV(y))
        res = [delistify(to_np(l))]
        res += [f(datafy(preds), datafy(y)) for f in metrics]
    stepper.reset(True)
    return res