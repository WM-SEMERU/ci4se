def _normalize_address_type(self, addr):
    addr_e = _raw_ast(addr)
    if isinstance(addr_e, (claripy.bv.BVV, claripy.vsa.StridedInterval,
        claripy.vsa.ValueSet)):
        raise SimMemoryError(
            '_normalize_address_type() does not take claripy models.')
    if isinstance(addr_e, claripy.ast.Base):
        if not isinstance(addr_e._model_vsa, ValueSet):
            addr_e = addr_e.annotate(RegionAnnotation('global', 0, addr_e.
                _model_vsa))
        return addr_e._model_vsa.items()
    else:
        raise SimAbstractMemoryError('Unsupported address type %s' % type(
            addr_e))