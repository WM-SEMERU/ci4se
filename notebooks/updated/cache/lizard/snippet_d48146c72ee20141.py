def connect(self, datas=None):
    if datas:
        self.connect_inputs(datas)
    postorder = self.postorder()
    self.log.debug('%s trying to connect in the order %s' % (repr(self),
        repr(postorder)))
    for piper in postorder:
        if not piper.connected and self[piper].nodes():
            inputs = [p for p in postorder if p in self[piper].nodes()]
            inputs.sort(cmp=self.children_after_parents)
            piper.connect(inputs)
    self.log.debug('%s succesfuly connected' % repr(self))