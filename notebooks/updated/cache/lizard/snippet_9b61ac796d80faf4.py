def apply_layout(self, child, layout):
    params = self.create_layout_params(child, layout)
    w = child.widget
    if w:
        if layout.get('padding'):
            dp = self.dp
            l, t, r, b = layout['padding']
            w.setPadding(int(l * dp), int(t * dp), int(r * dp), int(b * dp))
    child.layout_params = params