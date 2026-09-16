def evaluate_perceptron(ctx, model, corpus):
    click.echo('chemdataextractor.pos.evaluate')
    if corpus == 'wsj':
        evaluation = wsj_evaluation
        sents = list(evaluation.tagged_sents())
        for i, wsj_sent in enumerate(sents):
            sents[i] = [t for t in wsj_sent if not t[1] == '-NONE-']
    elif corpus == 'genia':
        evaluation = genia_evaluation
        sents = list(evaluation.tagged_sents())
        for i, genia_sent in enumerate(sents):
            for j, (token, tag) in enumerate(genia_sent):
                if tag == '(':
                    sents[i][j] = token, '-LRB-'
                elif tag == ')':
                    sents[i][j] = token, '-RRB-'
    else:
        raise click.ClickException('Invalid corpus')
    tagger = ChemApPosTagger(model=model)
    accuracy = tagger.evaluate(sents)
    click.echo('%s on %s: %s' % (model, evaluation, accuracy))