def get_output_base_path(self, output_directory, output_prefix,
    feature_type, overwrite):
    path = os.path.join(output_directory, '%s%s' % (output_prefix,
        feature_type))
    if overwrite:
        shp = '%s.shp' % path
        if os.path.isfile(shp):
            os.remove(shp)
    else:
        separator = '-'
        suffix = self.get_unique_file_path_suffix('%s.shp' % path, separator)
        if suffix:
            path = os.path.join(output_directory, '%s%s%s%s' % (
                output_prefix, feature_type, separator, suffix))
    return path