def load_api_folder(api_folder_path):
    api_definition_mapping = {}
    api_items_mapping = load_folder_content(api_folder_path)
    for api_file_path, api_items in api_items_mapping.items():
        if isinstance(api_items, list):
            for api_item in api_items:
                key, api_dict = api_item.popitem()
                api_id = api_dict.get('id') or api_dict.get('def'
                    ) or api_dict.get('name')
                if key != 'api' or not api_id:
                    raise exceptions.ParamsError('Invalid API defined in {}'
                        .format(api_file_path))
                if api_id in api_definition_mapping:
                    raise exceptions.ParamsError(
                        'Duplicated API ({}) defined in {}'.format(api_id,
                        api_file_path))
                else:
                    api_definition_mapping[api_id] = api_dict
        elif isinstance(api_items, dict):
            if api_file_path in api_definition_mapping:
                raise exceptions.ParamsError('Duplicated API defined: {}'.
                    format(api_file_path))
            else:
                api_definition_mapping[api_file_path] = api_items
    return api_definition_mapping