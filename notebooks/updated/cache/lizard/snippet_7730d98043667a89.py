def write_plugin_items(xml_tree, records, app_id, api_ver=3, app_ver=None):
    if not records:
        return
    pluginItems = etree.SubElement(xml_tree, 'pluginItems')
    for item in records:
        for versionRange in item.get('versionRange', []):
            if not versionRange.get('targetApplication'):
                add_plugin_item(pluginItems, item, versionRange, app_id=
                    app_id, api_ver=api_ver, app_ver=app_ver)
            else:
                targetApplication = get_related_targetApplication(versionRange,
                    app_id, app_ver)
                if targetApplication is not None:
                    add_plugin_item(pluginItems, item, versionRange,
                        targetApplication, app_id=app_id, api_ver=api_ver,
                        app_ver=app_ver)