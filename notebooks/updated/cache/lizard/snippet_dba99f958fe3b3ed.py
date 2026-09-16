def build_cards(jokers=False, num_jokers=0):
    new_deck = []
    if jokers:
        new_deck += [Card('Joker', None) for i in xrange(num_jokers)]
    new_deck += [Card(value, suit) for value in VALUES for suit in SUITS]
    return new_deck