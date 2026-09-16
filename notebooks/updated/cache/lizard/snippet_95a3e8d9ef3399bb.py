def spellcheck(self, words, suggestions=True):
    if isinstance(words, six.string_types):
        words = words.split()
    words = [convert(w) for w in words]
    spellresults = self._morf.spellcheck(words, suggestions)
    results = []
    for spellresult in spellresults:
        suggestions = [deconvert(s) for s in spellresult.suggestions]
        result = {'text': deconvert(spellresult.word), 'spelling':
            spellresult.spelling, 'suggestions': suggestions}
        results.append(result)
    return results