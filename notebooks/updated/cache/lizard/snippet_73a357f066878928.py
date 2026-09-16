def get_settings(self):
    postgame = self.get_postgame()
    return {'type': (self._header.lobby.game_type_id, self._header.lobby.
        game_type), 'difficulty': (self._header.scenario.game_settings.
        difficulty_id, self._header.scenario.game_settings.difficulty),
        'population_limit': self._header.lobby.population_limit * 25,
        'map_reveal_choice': (self._header.lobby.reveal_map_id, self.
        _header.lobby.reveal_map), 'speed': (self._header.replay.
        game_speed_id, mgz.const.SPEEDS.get(self._header.replay.
        game_speed_id)), 'cheats': self._header.replay.cheats_enabled,
        'lock_teams': self._header.lobby.lock_teams, 'starting_resources':
        (postgame.resource_level_id if postgame else None, postgame.
        resource_level if postgame else None), 'starting_age': (postgame.
        starting_age_id if postgame else None, postgame.starting_age if
        postgame else None), 'victory_condition': (postgame.victory_type_id if
        postgame else None, postgame.victory_type if postgame else None),
        'team_together': not postgame.team_together if postgame else None,
        'all_technologies': postgame.all_techs if postgame else None,
        'lock_speed': postgame.lock_speed if postgame else None,
        'multiqueue': None}