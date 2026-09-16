def pt_xml(self, values):
    xml = '                <c:ptCount val="{pt_count}"/>\n'.format(pt_count
        =len(values))
    pt_tmpl = """                <c:pt idx="{idx}">
                  <c:v>{value}</c:v>
                </c:pt>
"""
    for idx, value in enumerate(values):
        if value is None:
            continue
        xml += pt_tmpl.format(idx=idx, value=value)
    return xml