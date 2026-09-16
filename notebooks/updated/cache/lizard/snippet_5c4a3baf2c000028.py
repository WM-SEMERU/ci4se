def _update_aws_include_relative_path(template_dict, original_root, new_root):
    for key, val in template_dict.items():
        if key == 'Fn::Transform':
            if isinstance(val, dict) and val.get('Name') == 'AWS::Include':
                path = val.get('Parameters', {}).get('Location', {})
                updated_path = _resolve_relative_to(path, original_root,
                    new_root)
                if not updated_path:
                    continue
                val['Parameters']['Location'] = updated_path
        elif isinstance(val, dict):
            _update_aws_include_relative_path(val, original_root, new_root)
        elif isinstance(val, list):
            for item in val:
                if isinstance(item, dict):
                    _update_aws_include_relative_path(item, original_root,
                        new_root)
    return template_dict