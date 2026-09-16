def random_draft(card_class: CardClass, exclude=[]):
    from . import cards
    from .deck import Deck
    deck = []
    collection = []
    for card in cards.db.keys():
        if card in exclude:
            continue
        cls = cards.db[card]
        if not cls.collectible:
            continue
        if cls.type == CardType.HERO:
            continue
        if cls.card_class and cls.card_class not in [card_class, CardClass.
            NEUTRAL]:
            continue
        collection.append(cls)
    while len(deck) < Deck.MAX_CARDS:
        card = random.choice(collection)
        if deck.count(card.id) < card.max_count_in_deck:
            deck.append(card.id)
    return deck