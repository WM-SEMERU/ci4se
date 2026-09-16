def export_yaml(obj, file_name):

    def callback(data):
        stream = StringIO()
        yaml = YAML()
        yaml.dump(data, stream)
        return stream.getvalue()
    try:
        from ruamel.yaml import YAML
    except ImportError:
        raise exch.GeomdlException(
            "Please install 'ruamel.yaml' package to use YAML format: pip install ruamel.yaml"
            )
    exported_data = exch.export_dict_str(obj=obj, callback=callback)
    return exch.write_file(file_name, exported_data)