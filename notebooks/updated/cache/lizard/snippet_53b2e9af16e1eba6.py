def _parent_changed(self, parent):
    from .index_operations import ParameterIndexOperationsView
    offset = parent._offset_for(self)
    for name, iop in list(self._index_operations.items()):
        self.remove_index_operation(name)
        self.add_index_operation(name, ParameterIndexOperationsView(parent.
            _index_operations[name], offset, self.size))
    self._fixes_ = None
    for p in self.parameters:
        p._parent_changed(parent)