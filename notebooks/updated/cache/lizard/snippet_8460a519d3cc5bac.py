def _yield_exercises(self):
    for day in self.days:
        for dynamic_ex in day.dynamic_exercises:
            yield dynamic_ex
        for static_ex in day.static_exercises:
            yield static_ex