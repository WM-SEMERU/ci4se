def _calculate_fnr_fdr(group):
    data = {k: d['value'] for k, d in group.set_index('metric').T.to_dict()
        .items()}
    return pd.DataFrame([{'fnr': data['fn'] / float(data['tp'] + data['fn']
        ) * 100.0 if data['tp'] > 0 else 0.0, 'fdr': data['fp'] / float(
        data['tp'] + data['fp']) * 100.0 if data['tp'] > 0 else 0.0, 'tpr':
        'TP: %s FN: %s' % (data['tp'], data['fn']), 'spc': 'FP: %s' % data[
        'fp']}])