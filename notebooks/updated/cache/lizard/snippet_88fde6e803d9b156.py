def eventgroups(ctx, sport):
    sport = Sport(sport, peerplays_instance=ctx.peerplays)
    click.echo(pretty_print(sport.eventgroups, ctx=ctx))