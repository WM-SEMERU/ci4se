def create_masked_lm_predictions(tokens, masked_lm_prob,
    max_predictions_per_seq, vocab_words, rng):
    cand_indexes = []
    for i, token in enumerate(tokens):
        if token in ['[CLS]', '[SEP]']:
            continue
        cand_indexes.append(i)
    rng.shuffle(cand_indexes)
    output_tokens = list(tokens)
    num_to_predict = min(max_predictions_per_seq, max(1, int(round(len(
        tokens) * masked_lm_prob))))
    masked_lms = []
    covered_indexes = set()
    for index in cand_indexes:
        if len(masked_lms) >= num_to_predict:
            break
        if index in covered_indexes:
            continue
        covered_indexes.add(index)
        masked_token = None
        if rng.random() < 0.8:
            masked_token = '[MASK]'
        elif rng.random() < 0.5:
            masked_token = tokens[index]
        else:
            masked_token = vocab_words[rng.randint(0, len(vocab_words) - 1)]
        output_tokens[index] = masked_token
        masked_lms.append(MaskedLmInstance(index=index, label=tokens[index]))
    masked_lms = sorted(masked_lms, key=lambda x: x.index)
    masked_lm_positions = []
    masked_lm_labels = []
    for p in masked_lms:
        masked_lm_positions.append(p.index)
        masked_lm_labels.append(p.label)
    return output_tokens, masked_lm_positions, masked_lm_labels