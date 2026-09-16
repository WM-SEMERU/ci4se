def update(self):
    if self.time_left > 0:
        self.time_left -= 1
        for _ in range(self._count):
            new_particle = self._new_particle()
            if new_particle is not None:
                self.particles.append(new_particle)
    for particle in self.particles:
        last = particle.last()
        if last is not None:
            char, x, y, fg, attr, bg = last
            screen_data = self._screen.get_from(x, y)
            if self._blend and screen_data:
                index = self._find_colour(particle, 0, screen_data) - 1
                fg, attr, bg = particle.colours[max(index, 0)]
            self._screen.print_at(' ', x, y, fg, attr, bg)
        if particle.time < particle.life_time:
            char, x, y, fg, attr, bg = particle.next()
            screen_data = self._screen.get_from(x, y)
            if self._blend and screen_data:
                index = self._find_colour(particle, -1, screen_data) + 1
                fg, attr, bg = particle.colours[min(index, len(particle.
                    colours) - 1)]
            self._screen.print_at(char, x, y, fg, attr, bg)
        else:
            self.particles.remove(particle)