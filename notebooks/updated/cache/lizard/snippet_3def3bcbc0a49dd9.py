def _proc_cyclic(self):
    main_axis, rot = max(self.rot_sym, key=lambda v: v[1])
    self.sch_symbol = 'C{}'.format(rot)
    mirror_type = self._find_mirror(main_axis)
    if mirror_type == 'h':
        self.sch_symbol += 'h'
    elif mirror_type == 'v':
        self.sch_symbol += 'v'
    elif mirror_type == '':
        if self.is_valid_op(SymmOp.rotoreflection(main_axis, angle=180 / rot)):
            self.sch_symbol = 'S{}'.format(2 * rot)