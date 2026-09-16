def dequeue(ctx):
    tweet = ctx.obj['TWEETLIST'].peek()
    if tweet is None:
        click.echo('Nothing to dequeue.')
        ctx.exit(1)
    if ctx.obj['DRYRUN']:
        click.echo(tweet)
    else:
        tweet = ctx.obj['TWEETLIST'].pop()
        ctx.obj['TWEEPY_API'].update_status(tweet)