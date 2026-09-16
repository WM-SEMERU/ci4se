def composition_prediction(self, composition, to_this_composition=True):
    preds = self.list_prediction(list(composition.keys()), to_this_composition)
    output = []
    for p in preds:
        if to_this_composition:
            subs = {v: k for k, v in p['substitutions'].items()}
        else:
            subs = p['substitutions']
        charge = 0
        for k, v in composition.items():
            charge += subs[k].oxi_state * v
        if abs(charge) < 1e-08:
            output.append(p)
    logging.info('{} charge balanced substitutions found'.format(len(output)))
    return output