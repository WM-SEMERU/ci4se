def from_textfile(cls, textfile, workers=1, job_size=1000):
    c = Counter()
    if isinstance(textfile, string_types):
        textfile = TextFile(textfile)
    for result in textfile.apply(count, workers, job_size):
        c.update(result)
    return CountedVocabulary(word_count=c)