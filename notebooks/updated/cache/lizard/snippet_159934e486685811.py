def points_properties_df(self):
    pprops = {}
    for each in self.points:
        p = each.properties.asdict.copy()
        p.pop('device', None)
        p.pop('network', None)
        p.pop('simulated', None)
        p.pop('overridden', None)
        pprops[each.properties.name] = p
    df = pd.DataFrame(pprops)
    return df