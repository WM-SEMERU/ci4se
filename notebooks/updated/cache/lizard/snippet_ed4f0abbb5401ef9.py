def _score_for_model(meta):
    mean_acc = list()
    pipes = meta['pipeline']
    acc = meta['accuracy']
    if 'tagger' in pipes:
        mean_acc.append(acc['tags_acc'])
    if 'parser' in pipes:
        mean_acc.append((acc['uas'] + acc['las']) / 2)
    if 'ner' in pipes:
        mean_acc.append((acc['ents_p'] + acc['ents_r'] + acc['ents_f']) / 3)
    return sum(mean_acc) / len(mean_acc)