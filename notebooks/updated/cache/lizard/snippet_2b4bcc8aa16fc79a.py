def _parse_player_position(self, player_info):
    for section in player_info('div#meta p').items():
        if 'Position' in str(section):
            position = section.text().replace('Position: ', '')
            setattr(self, '_position', position)
            break