def check_fault_data(cls, fault_trace, upper_seismogenic_depth,
    lower_seismogenic_depth, dip, mesh_spacing):
    if not len(fault_trace) >= 2:
        raise ValueError('the fault trace must have at least two points')
    if not fault_trace.horizontal():
        raise ValueError('the fault trace must be horizontal')
    tlats = [point.latitude for point in fault_trace.points]
    tlons = [point.longitude for point in fault_trace.points]
    if geo_utils.line_intersects_itself(tlons, tlats):
        raise ValueError('fault trace intersects itself')
    if not 0.0 < dip <= 90.0:
        raise ValueError('dip must be between 0.0 and 90.0')
    if not lower_seismogenic_depth > upper_seismogenic_depth:
        raise ValueError(
            'lower seismogenic depth must be greater than upper seismogenic depth'
            )
    if not upper_seismogenic_depth >= fault_trace[0].depth:
        raise ValueError(
            'upper seismogenic depth must be greater than or equal to depth of fault trace'
            )
    if not mesh_spacing > 0.0:
        raise ValueError('mesh spacing must be positive')