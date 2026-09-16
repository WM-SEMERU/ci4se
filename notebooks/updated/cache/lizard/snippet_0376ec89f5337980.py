def _parseDataDirectory(self, data, sections, imageNtHeaders):
    data_directory_data_list = [None for i in range(15)]
    export_data_directory = imageNtHeaders.header.OptionalHeader.DataDirectory[
        ImageDirectoryEntry.EXPORT]
    export_section = self._getSectionForDataDirectoryEntry(
        export_data_directory, sections)
    export_data_directory_data = self._parseDataDirectoryExport(data,
        export_data_directory, export_section)
    data_directory_data_list[ImageDirectoryEntry.EXPORT
        ] = export_data_directory_data
    import_data_directory = imageNtHeaders.header.OptionalHeader.DataDirectory[
        ImageDirectoryEntry.IMPORT]
    import_section = self._getSectionForDataDirectoryEntry(
        import_data_directory, sections)
    import_data_directory_data = self._parseDataDirectoryImport(
        import_data_directory, import_section)
    data_directory_data_list[ImageDirectoryEntry.IMPORT
        ] = import_data_directory_data
    loadconfig_data_directory = (imageNtHeaders.header.OptionalHeader.
        DataDirectory[ImageDirectoryEntry.LOAD_CONFIG])
    loadconfig_section = self._getSectionForDataDirectoryEntry(
        loadconfig_data_directory, sections)
    loadconfig_data = self._parseLoadConfig(loadconfig_data_directory,
        loadconfig_section)
    data_directory_data_list[ImageDirectoryEntry.LOAD_CONFIG] = loadconfig_data
    return data_directory_data_list