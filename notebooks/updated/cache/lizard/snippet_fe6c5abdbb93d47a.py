def recall_score(y_true, y_pred, average='micro', suffix=False):
    true_entities = set(get_entities(y_true, suffix))
    pred_entities = set(get_entities(y_pred, suffix))
    nb_correct = len(true_entities & pred_entities)
    nb_true = len(true_entities)
    score = nb_correct / nb_true if nb_true > 0 else 0
    return score