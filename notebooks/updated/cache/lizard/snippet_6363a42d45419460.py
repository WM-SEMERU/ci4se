def register_plugin(manager):
    manager.register_blueprint(player)
    manager.register_mimetype_function(detect_playable_mimetype)
    manager.register_widget(place='styles', type='stylesheet', endpoint=
        'player.static', filename='css/browse.css')
    manager.register_widget(place='entry-link', type='link', endpoint=
        'player.audio', filter=PlayableFile.detect)
    manager.register_widget(place='entry-link', icon='playlist', type=
        'link', endpoint='player.playlist', filter=PlayListFile.detect)
    manager.register_widget(place='entry-actions', css='play', type=
        'button', endpoint='player.audio', filter=PlayableFile.detect)
    manager.register_widget(place='entry-actions', css='play', type=
        'button', endpoint='player.playlist', filter=PlayListFile.detect)
    if manager.get_argument('player_directory_play'):
        manager.register_widget(place='header', type='button', endpoint=
            'player.directory', text='Play directory', filter=
            PlayableDirectory.detect)