def draw_actions(self):
    now = time.time()
    for act in self._past_actions:
        if act.pos and now < act.deadline:
            remain = (act.deadline - now) / (act.deadline - act.time)
            if isinstance(act.pos, point.Point):
                size = remain / 3
                self.all_surfs(_Surface.draw_circle, act.color, act.pos,
                    size, 1)
            else:
                self.all_surfs(_Surface.draw_rect, act.color, act.pos, 1)