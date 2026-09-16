def convert_list_elements(self):
    for list_el in self.main.getroot().findall('.//list'):
        if list_el.getparent().tag == 'p':
            elevate_element(list_el)
    for list_el in self.main.getroot().findall('.//list'):
        if 'list-type' not in list_el.attrib:
            list_el_type = 'order'
        else:
            list_el_type = list_el.attrib['list-type']
        if list_el_type in ['', 'bullet', 'simple']:
            list_el.tag = 'ul'
            if list_el_type == 'simple':
                list_el.attrib['class'] = 'simple'
        else:
            list_el.tag = 'ol'
            list_el.attrib['class'] = list_el_type
        for list_item in list_el.findall('list-item'):
            list_item.tag = 'li'
        remove_all_attributes(list_el, exclude=['id', 'class'])