def _ensure_panel_ids(dashboard):
    panel_id = 1
    for row in dashboard.get('rows', []):
        for panel in row.get('panels', []):
            panel['id'] = panel_id
            panel_id += 1