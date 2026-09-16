def eval_model(model, test, add_eval_metrics={}):
    logger.info('Evaluate...')
    model_metrics_values = model.evaluate(test[0], test[1], verbose=0,
        batch_size=test[1].shape[0])
    model_metrics = dict(zip(_listify(model.metrics_names), _listify(
        model_metrics_values)))
    y_true = test[1]
    y_pred = model.predict(test[0], verbose=0)
    eval_metrics = {k: v(y_true, y_pred) for k, v in add_eval_metrics.items()}
    intersected_keys = set(model_metrics).intersection(set(eval_metrics))
    if len(intersected_keys) > 0:
        logger.warning(
            'Some metric names intersect: {0}. Ignoring the add_eval_metrics ones'
            .format(intersected_keys))
        eval_metrics = _delete_keys(eval_metrics, intersected_keys)
    return merge_dicts(model_metrics, eval_metrics)