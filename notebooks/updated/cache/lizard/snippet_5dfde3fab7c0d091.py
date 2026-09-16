def _load_nested_libraries(self, library_path, target_dict):
    for library_name in os.listdir(library_path):
        library_folder_path, library_name = self.check_clean_path_of_library(
            library_path, library_name)
        full_library_path = os.path.join(library_path, library_name)
        if os.path.isdir(full_library_path) and library_name[0] != '.':
            if os.path.exists(os.path.join(full_library_path, storage.
                STATEMACHINE_FILE)) or os.path.exists(os.path.join(
                full_library_path, storage.STATEMACHINE_FILE_OLD)):
                target_dict[library_name] = full_library_path
            else:
                target_dict[library_name] = {}
                self._load_nested_libraries(full_library_path, target_dict[
                    library_name])
                target_dict[library_name] = OrderedDict(sorted(target_dict[
                    library_name].items()))