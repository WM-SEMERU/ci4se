def box_model_domain(num_points=2, **kwargs):
    ax = Axis(axis_type='abstract', num_points=num_points)
    boxes = _Domain(axes=ax, **kwargs)
    boxes.domain_type = 'box'
    return boxes