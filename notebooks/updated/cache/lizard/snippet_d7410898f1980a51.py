def staking_leaderboard(round_num=0, tournament=1):
    click.echo(prettify(napi.get_staking_leaderboard(tournament=tournament,
        round_num=round_num)))