def add_book(self, publisher=None, place=None, date=None):
    imprint = {}
    if date is not None:
        imprint['date'] = normalize_date(date)
    if place is not None:
        imprint['place'] = place
    if publisher is not None:
        imprint['publisher'] = publisher
    self._append_to('imprints', imprint)