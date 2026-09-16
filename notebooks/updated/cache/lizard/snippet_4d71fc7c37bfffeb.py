def _get_summary(self, text, **kwargs):
    card = cards.extract_card(text, kwargs, self.search_path)
    return flask.Markup((card.description or '').strip())