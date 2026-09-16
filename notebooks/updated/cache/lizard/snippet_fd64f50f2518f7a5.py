def _CurrentAuditLog():
    now_sec = rdfvalue.RDFDatetime.Now().AsSecondsSinceEpoch()
    rollover_seconds = AUDIT_ROLLOVER_TIME.seconds
    current_log = now_sec // rollover_seconds * rollover_seconds
    return _AuditLogBase().Add(str(current_log))