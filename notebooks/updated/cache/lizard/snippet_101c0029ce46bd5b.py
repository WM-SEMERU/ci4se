def _ProcessFileEntry(self, mediator, file_entry):
    display_name = mediator.GetDisplayName()
    logger.debug('[ProcessFileEntry] processing file entry: {0:s}'.format(
        display_name))
    reference_count = mediator.resolver_context.GetFileObjectReferenceCount(
        file_entry.path_spec)
    try:
        if self._IsMetadataFile(file_entry):
            self._ProcessMetadataFile(mediator, file_entry)
        else:
            file_entry_processed = False
            for data_stream in file_entry.data_streams:
                if self._abort:
                    break
                if self._CanSkipDataStream(file_entry, data_stream):
                    logger.debug(
                        '[ProcessFileEntry] Skipping datastream {0:s} for {1:s}: {2:s}'
                        .format(data_stream.name, file_entry.type_indicator,
                        display_name))
                    continue
                self._ProcessFileEntryDataStream(mediator, file_entry,
                    data_stream)
                file_entry_processed = True
            if not file_entry_processed:
                self._ProcessFileEntryDataStream(mediator, file_entry, None)
    finally:
        new_reference_count = (mediator.resolver_context.
            GetFileObjectReferenceCount(file_entry.path_spec))
        if reference_count != new_reference_count:
            if mediator.resolver_context.ForceRemoveFileObject(file_entry.
                path_spec):
                logger.warning(
                    'File-object not explicitly closed for file: {0:s}'.
                    format(display_name))
    logger.debug('[ProcessFileEntry] done processing file entry: {0:s}'.
        format(display_name))