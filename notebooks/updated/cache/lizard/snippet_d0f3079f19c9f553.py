def calc_update_events(self, asin_to_progress):
    new_events = []
    for asin, new_progress in asin_to_progress.iteritems():
        try:
            book_snapshot = self.get_book(asin)
        except KeyError:
            new_events.append(AddEvent(asin))
        else:
            if book_snapshot.status == ReadingStatus.CURRENT:
                change = new_progress - book_snapshot.progress
                if change > 0:
                    new_events.append(ReadEvent(asin, change))
    return new_events