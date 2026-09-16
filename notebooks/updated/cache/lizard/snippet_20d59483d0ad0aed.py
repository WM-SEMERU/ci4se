def _CreateFolder(self, parent, name, visible=True, description=None):
    folder = ET.SubElement(parent, 'Folder')
    name_tag = ET.SubElement(folder, 'name')
    name_tag.text = name
    if description is not None:
        desc_tag = ET.SubElement(folder, 'description')
        desc_tag.text = description
    if not visible:
        visibility = ET.SubElement(folder, 'visibility')
        visibility.text = '0'
    return folder