def get_template_id(template_name, auth, url):
    object_list = get_cfg_template(auth=auth, url=url)
    for template in object_list:
        if template['confFileName'] == template_name:
            return int(template['confFileId'])
    return 'template not found'