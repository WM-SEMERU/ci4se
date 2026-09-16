def find(self, text):
    genres = []
    text = text.lower()
    category_counter = Counter()
    counter = Counter()
    for genre in self.db.genres:
        found = self.contains_entity(genre, text)
        if found:
            counter[genre] += found
            category = self.db.reference[genre]
            points = self.db.points[genre]
            points *= found
            if category_counter[category] > 0:
                points += 1
            category_counter[category] += points
    for tag in self.db.tags:
        found = self.contains_entity(tag, text)
        if found:
            category = self.db.reference[tag]
            if not counter[category]:
                counter[category] += found
            points = self.db.points[tag]
            points *= found
            category_counter[category] += points
    if not category_counter:
        return genres
    main_category = category_counter.most_common(1)[0][0]
    sorted_genres = [ite for ite, it in counter.most_common()]
    for genre in sorted_genres:
        insert = True
        if self.unique_category:
            if not self.db.reference[genre] == main_category:
                insert = False
        if insert:
            genres.append(genre)
    return genres