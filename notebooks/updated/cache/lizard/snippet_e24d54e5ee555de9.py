def _ProcessPathSpec(self, extraction_worker, parser_mediator, path_spec):
    self._current_display_name = parser_mediator.GetDisplayNameForPathSpec(
        path_spec)
    try:
        extraction_worker.ProcessPathSpec(parser_mediator, path_spec)
    except KeyboardInterrupt:
        self._abort = True
        self._processing_status.aborted = True
        if self._status_update_callback:
            self._status_update_callback(self._processing_status)
    except dfvfs_errors.CacheFullError:
        self._abort = True
        logger.error(
            'ABORT: detected cache full error while processing path spec: {0:s}'
            .format(self._current_display_name))
    except Exception as exception:
        parser_mediator.ProduceExtractionWarning(
            'unable to process path specification with error: {0!s}'.format
            (exception), path_spec=path_spec)
        if getattr(self._processing_configuration, 'debug_output', False):
            logger.warning(
                'Unhandled exception while processing path spec: {0:s}.'.
                format(self._current_display_name))
            logger.exception(exception)
            pdb.post_mortem()