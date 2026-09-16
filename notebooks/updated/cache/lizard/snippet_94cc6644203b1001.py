def term_count_buckets(self):
    buckets = {}
    for term, count in self.term_counts().items():
        if count in buckets:
            buckets[count].append(term)
        else:
            buckets[count] = [term]
    return buckets