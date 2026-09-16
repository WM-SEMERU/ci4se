def _CreatePlacemark(self, parent, name, style_id=None, visible=True,
    description=None):
    placemark = ET.SubElement(parent, 'Placemark')
    placemark_name = ET.SubElement(placemark, 'name')
    placemark_name.text = name
    if description is not None:
        desc_tag = ET.SubElement(placemark, 'description')
        desc_tag.text = description
    if style_id is not None:
        styleurl = ET.SubElement(placemark, 'styleUrl')
        styleurl.text = '#%s' % style_id
    if not visible:
        visibility = ET.SubElement(placemark, 'visibility')
        visibility.text = '0'
    return placemark