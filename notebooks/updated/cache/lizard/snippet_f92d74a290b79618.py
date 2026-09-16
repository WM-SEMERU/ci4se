def top_cards(self, number=1, cache=True, remove=True):
    getter = partial(self.get_card(cache=cache, remove=remove))
    return [getter(index=i) for i in range(number)]