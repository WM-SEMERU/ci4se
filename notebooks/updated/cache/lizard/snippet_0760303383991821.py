def calculate_width_widget(width, margin=None, margin_left=None,
    margin_right=None):
    if margin_left is None:
        margin_left = margin
    if margin_right is None:
        margin_right = margin
    if margin_left is not None:
        width -= int(margin_left)
    if margin_right is not None:
        width -= int(margin_right)
    return width if width > 0 else None