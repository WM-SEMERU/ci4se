def _check_Vn(self):
    if hasattr(self, 'bus') and hasattr(self, 'Vn'):
        bus_Vn = self.read_data_ext('Bus', field='Vn', idx=self.bus)
        for name, bus, Vn, Vn0 in zip(self.name, self.bus, self.Vn, bus_Vn):
            if Vn != Vn0:
                self.log('<{}> has Vn={} different from bus <{}> Vn={}.'.
                    format(name, Vn, bus, Vn0), WARNING)
    if hasattr(self, 'node') and hasattr(self, 'Vdcn'):
        node_Vdcn = self.read_data_ext('Node', field='Vdcn', idx=self.node)
        for name, node, Vdcn, Vdcn0 in zip(self.name, self.node, self.Vdcn,
            node_Vdcn):
            if Vdcn != Vdcn0:
                self.log('<{}> has Vdcn={} different from node <{}> Vdcn={}.'
                    .format(name, Vdcn, node, Vdcn0), WARNING)