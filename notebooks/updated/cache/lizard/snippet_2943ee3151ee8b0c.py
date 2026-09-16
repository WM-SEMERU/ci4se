def train_all(ctx, output):
    click.echo('chemdataextractor.pos.train_all')
    click.echo('Output: %s' % output)
    ctx.invoke(train, output='%s_wsj_nocluster.pickle' % output, corpus=
        'wsj', clusters=False)
    ctx.invoke(train, output='%s_wsj.pickle' % output, corpus='wsj',
        clusters=True)
    ctx.invoke(train, output='%s_genia_nocluster.pickle' % output, corpus=
        'genia', clusters=False)
    ctx.invoke(train, output='%s_genia.pickle' % output, corpus='genia',
        clusters=True)
    ctx.invoke(train, output='%s_wsj_genia_nocluster.pickle' % output,
        corpus='wsj+genia', clusters=False)
    ctx.invoke(train, output='%s_wsj_genia.pickle' % output, corpus=
        'wsj+genia', clusters=True)