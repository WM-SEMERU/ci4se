def tag(ctx, model, cs, corpus, output):
    click.echo('chemdataextractor.dict.tag')
    tagger = CsDictCemTagger(model=model) if cs else CiDictCemTagger(model=
        model)
    for line in corpus:
        sentence = []
        goldsentence = []
        for t in line.split():
            token, tag = t.rsplit('/', 1)
            goldsentence.append((token, tag))
            sentence.append(token)
        if sentence:
            tokentags = tagger.tag(sentence)
            for i, tokentag in enumerate(tokentags):
                goldtokentag = goldsentence[i]
                if goldtokentag[1] not in {'B-CM', 'I-CM'} and tokentag[1] in {
                    'B-CM', 'I-CM'}:
                    print(line)
                    print(tokentag[0])
            output.write(' '.join('/'.join(tokentag) for tokentag in tagger
                .tag(sentence)))
            output.write('\n')
        else:
            output.write('\n')