def _handle_dbproc_call(self, parts, parameters_metadata):
    for part in parts:
        if part.kind == part_kinds.ROWSAFFECTED:
            self.rowcount = part.values[0]
        elif part.kind == part_kinds.TRANSACTIONFLAGS:
            pass
        elif part.kind == part_kinds.STATEMENTCONTEXT:
            pass
        elif part.kind == part_kinds.OUTPUTPARAMETERS:
            self._buffer = part.unpack_rows(parameters_metadata, self.
                connection)
            self._received_last_resultset_part = True
            self._executed = True
        elif part.kind == part_kinds.RESULTSETMETADATA:
            self.description, self._column_types = (self.
                _handle_result_metadata(part))
        elif part.kind == part_kinds.RESULTSETID:
            self._resultset_id = part.value
        elif part.kind == part_kinds.RESULTSET:
            self._buffer = part.unpack_rows(self._column_types, self.connection
                )
            self._received_last_resultset_part = part.attribute & 1
            self._executed = True
        else:
            raise InterfaceError(
                'Stored procedure call, unexpected part kind %d.' % part.kind)
    self._executed = True