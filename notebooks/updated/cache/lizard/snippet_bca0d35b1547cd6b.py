def draw_overlay(self, surf):
    obs = self._obs.observation
    player = obs.player_common
    surf.write_screen(self._font_large, colors.green, (0.2, 0.2), 
        'Minerals: %s, Vespene: %s, Food: %s / %s' % (player.minerals,
        player.vespene, player.food_used, player.food_cap))
    times, steps = zip(*self._game_times)
    sec = obs.game_loop // 22.4
    surf.write_screen(self._font_large, colors.green, (-0.2, 0.2), 
        'Score: %s, Step: %s, %.1f/s, Time: %d:%02d' % (obs.score.score,
        obs.game_loop, sum(steps) / (sum(times) or 1), sec // 60, sec % 60),
        align='right')
    surf.write_screen(self._font_large, colors.green * 0.8, (-0.2, 1.2), 
        'FPS: O:%.1f, R:%.1f' % (len(times) / (sum(times) or 1), len(self.
        _render_times) / (sum(self._render_times) or 1)), align='right')
    line = 3
    for alert, ts in sorted(self._alerts.items(), key=lambda item: item[1]):
        if time.time() < ts + 3:
            surf.write_screen(self._font_large, colors.red, (20, line), alert)
            line += 1
        else:
            del self._alerts[alert]