def build_components(components):
    component_list = []
    for comp in components:
        component = ea.Component()
        component.id = comp.get('id')
        component.type = comp.get('type')
        component.asset = comp.get('asset')
        component.doi = comp.get('doi')
        if component_title(comp) != '':
            component.title = component_title(comp)
        if comp.get('type') in ['supplementary-material', 'fig']:
            if comp.get('full_caption'):
                subtitle = comp.get('full_caption')
                subtitle = clean_abstract(subtitle)
                component.subtitle = subtitle
        if comp.get('type') in ['abstract', 'table-wrap', 'sub-article',
            'chem-struct-wrap', 'boxed-text']:
            component.mime_type = 'text/plain'
        if comp.get('type') in ['fig']:
            component.mime_type = 'image/tiff'
        elif comp.get('type') in ['media', 'supplementary-material']:
            if comp.get('mimetype') and comp.get('mime-subtype'):
                component.mime_type = comp.get('mimetype') + '/' + comp.get(
                    'mime-subtype')
        component.permissions = comp.get('permissions')
        component_list.append(component)
    return component_list