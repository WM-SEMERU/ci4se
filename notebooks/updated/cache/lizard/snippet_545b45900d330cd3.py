def register_palette(self):
    default = 'default'
    palette = list(self.palette)
    mapping = CONFIG['rgb_to_short']
    for tok in self.style.styles.keys():
        for t in tok.split()[::-1]:
            st = self.style.styles[t]
            if '#' in st:
                break
        if '#' not in st:
            st = ''
        st = st.split()
        st.sort()
        if len(st) == 0:
            c = default
        elif st[0].startswith('bg:'):
            c = default
        elif len(st[0]) == 7:
            c = 'h' + rgb_to_short(st[0][1:], mapping)[0]
        elif len(st[0]) == 4:
            c = 'h' + rgb_to_short(st[0][1] * 2 + st[0][2] * 2 + st[0][3] *
                2, mapping)[0]
        else:
            c = default
        a = urwid.AttrSpec(c, default, colors=256)
        row = tok, default, default, default, a.foreground, default
        palette.append(row)
    self.loop.screen.register_palette(palette)