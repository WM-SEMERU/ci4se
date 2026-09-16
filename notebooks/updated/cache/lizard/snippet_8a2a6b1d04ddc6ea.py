def _get_bmdl_ratio(self, models):
    bmdls = [model.output['BMDL'] for model in models if model.output[
        'BMDL'] > 0]
    return max(bmdls) / min(bmdls) if len(bmdls) > 0 else 0