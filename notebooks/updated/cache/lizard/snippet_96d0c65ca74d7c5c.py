def process_event(self, c):
    if c == '\x04':
        sys.exit()
    elif c in key_directions:
        self.move_entity(self.player, *vscale(self.player.speed,
            key_directions[c]))
    else:
        return 'try arrow keys, w, a, s, d, or ctrl-D (you pressed %r)' % c
    return self.tick()