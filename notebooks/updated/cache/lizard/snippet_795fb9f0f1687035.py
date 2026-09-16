def box_score(game_id):
    data = mlbgame.game.box_score(game_id)
    obj = mlbgame.game.GameBoxScore(data)
    return obj