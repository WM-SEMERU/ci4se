def get_F1_EM(dataset, predict_data):
    f1 = exact_match = total = 0
    for record in dataset:
        total += 1
        if record[1] not in predict_data:
            message = 'Unanswered question ' + record[1
                ] + ' will receive score 0.'
            print(message)
            continue
        ground_truths = record[4]
        prediction = predict_data[record[1]]
        exact_match += metric_max_over_ground_truths(exact_match_score,
            prediction, ground_truths)
        f1 += metric_max_over_ground_truths(f1_score, prediction, ground_truths
            )
    exact_match = 100.0 * exact_match / total
    f1 = 100.0 * f1 / total
    scores = {'exact_match': exact_match, 'f1': f1}
    return scores