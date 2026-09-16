def words_with_votes(self, only_topics=True):
    result = Word.objects.filter(bingofield__board__game__id=self.id).exclude(
        type=WORD_TYPE_MIDDLE)
    if only_topics:
        result = result.exclude(bingofield__word__type=WORD_TYPE_META)
    result = result.annotate(votes=Sum('bingofield__vote')).order_by('-votes'
        ).values()
    for item in result:
        item['votes'] = max(0, item['votes'])
        if result[0]['votes'] != 0:
            item['percent'] = float(item['votes']) / result[0]['votes'] * 100
        else:
            item['percent'] = 0
    return result