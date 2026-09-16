def check(text):
    err = 'consistency.spelling'
    msg = "Inconsistent spelling of '{}' (vs. '{}')."
    word_pairs = [['advisor', 'adviser'], ['centre', 'center'], ['colour',
        'color'], ['emphasise', 'emphasize'], ['finalise', 'finalize'], [
        'focussed', 'focused'], ['labour', 'labor'], ['learnt', 'learned'],
        ['organise', 'organize'], ['organised', 'organized'], ['organising',
        'organizing'], ['recognise', 'recognize']]
    return consistency_check(text, word_pairs, err, msg)