def _swap_gate(self, lines, ctrl_lines):
    delta_pos = self._gate_offset(SWAP)
    gate_width = self._gate_width(SWAP)
    lines.sort()
    gate_str = ''
    for line in lines:
        op = self._op(line)
        w = '{}cm'.format(0.5 * gate_width)
        s1 = '[xshift=-{w},yshift=-{w}]{op}.center'.format(w=w, op=op)
        s2 = '[xshift={w},yshift={w}]{op}.center'.format(w=w, op=op)
        s3 = '[xshift=-{w},yshift={w}]{op}.center'.format(w=w, op=op)
        s4 = '[xshift={w},yshift=-{w}]{op}.center'.format(w=w, op=op)
        swap_style = 'swapstyle,edgestyle'
        if self.settings['gate_shadow']:
            swap_style += ',shadowed'
        gate_str += (
            """
\\node[swapstyle] ({op}) at ({pos},-{line}) {{}};
\\draw[{swap_style}] ({s1})--({s2});
\\draw[{swap_style}] ({s3})--({s4});"""
            .format(op=op, s1=s1, s2=s2, s3=s3, s4=s4, line=line, pos=self.
            pos[line], swap_style=swap_style))
    gate_str += self._line(lines[0], lines[1])
    all_lines = ctrl_lines + lines
    new_pos = self.pos[lines[0]] + delta_pos + gate_width
    for i in all_lines:
        self.op_count[i] += 1
    for i in range(min(all_lines), max(all_lines) + 1):
        self.pos[i] = new_pos
    return gate_str