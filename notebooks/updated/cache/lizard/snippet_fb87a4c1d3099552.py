def parse_uncertainty_value(self, node, branchset):
    if branchset.uncertainty_type == 'sourceModel':
        return node.text.strip()
    elif branchset.uncertainty_type == 'abGRAbsolute':
        [a, b] = node.text.strip().split()
        return float(a), float(b)
    elif branchset.uncertainty_type == 'incrementalMFDAbsolute':
        min_mag, bin_width = node.incrementalMFD['minMag'
            ], node.incrementalMFD['binWidth']
        return min_mag, bin_width, ~node.incrementalMFD.occurRates
    elif branchset.uncertainty_type == 'simpleFaultGeometryAbsolute':
        return self._parse_simple_fault_geometry_surface(node.
            simpleFaultGeometry)
    elif branchset.uncertainty_type == 'complexFaultGeometryAbsolute':
        return self._parse_complex_fault_geometry_surface(node.
            complexFaultGeometry)
    elif branchset.uncertainty_type == 'characteristicFaultGeometryAbsolute':
        surfaces = []
        for geom_node in node.surface:
            if 'simpleFaultGeometry' in geom_node.tag:
                trace, usd, lsd, dip, spacing = (self.
                    _parse_simple_fault_geometry_surface(geom_node))
                surfaces.append(geo.SimpleFaultSurface.from_fault_data(
                    trace, usd, lsd, dip, spacing))
            elif 'complexFaultGeometry' in geom_node.tag:
                edges, spacing = self._parse_complex_fault_geometry_surface(
                    geom_node)
                surfaces.append(geo.ComplexFaultSurface.from_fault_data(
                    edges, spacing))
            elif 'planarSurface' in geom_node.tag:
                surfaces.append(self._parse_planar_geometry_surface(geom_node))
            else:
                pass
        if len(surfaces) > 1:
            return geo.MultiSurface(surfaces)
        else:
            return surfaces[0]
    else:
        return float(node.text.strip())