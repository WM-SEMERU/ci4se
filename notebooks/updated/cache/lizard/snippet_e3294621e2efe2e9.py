def get_negation(event):
    states = event.get('states', [])
    if not states:
        return []
    negs = [state for state in states if state.get('type') == 'NEGATION']
    neg_texts = [neg['text'] for neg in negs]
    return neg_texts