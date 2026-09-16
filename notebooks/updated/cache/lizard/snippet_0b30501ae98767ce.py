def assert_single_path_by_glob(self, components):
    glob_path_string = os.path.join(*components)
    expanded_glob = glob.glob(glob_path_string)
    try:
        return assert_single_element(expanded_glob)
    except StopIteration as e:
        raise self.ArchiveFileMappingError(
            "No elements for glob '{}' -- expected exactly one.".format(
            glob_path_string), e)
    except ValueError as e:
        raise self.ArchiveFileMappingError(
            "Should have exactly one path matching expansion of glob '{}'."
            .format(glob_path_string), e)