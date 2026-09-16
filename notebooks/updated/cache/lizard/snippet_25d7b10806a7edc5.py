def _complete_execution(self, g):
    assert g.ready()
    self.greenlets.remove(g)
    placed = UserCritical(msg='placeholder bogus exception', hint=
        'report a bug')
    if g.successful():
        try:
            segment = g.get()
            if not segment.explicit:
                segment.mark_done()
        except BaseException as e:
            placed = e
        else:
            placed = None
    else:
        placed = g.exception
    self.wait_change.put(placed)