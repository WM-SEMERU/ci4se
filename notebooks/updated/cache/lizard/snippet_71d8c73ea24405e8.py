def find_for_player_id(player_id, connection=None, page_size=100,
    page_number=0, sort_by=DEFAULT_SORT_BY, sort_order=DEFAULT_SORT_ORDER):
    return pybrightcove.connection.ItemResultSet('find_playlists_for_player_id'
        , Playlist, connection, page_size, page_number, sort_by, sort_order,
        player_id=player_id)